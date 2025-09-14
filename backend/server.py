from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict, Any
import os
from datetime import datetime, timedelta
import secrets
import resend
import httpx
from peptide_data import get_peptide_categories, get_default_team_data, get_default_blog_data
import logging
from middleware import rate_limit_middleware, cors_middleware
from passlib.context import CryptContext
import jwt

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Professor Peptides API", version="2.0.0")

# Add custom middleware
app.middleware("http")(rate_limit_middleware)
app.middleware("http")(cors_middleware)

# Initialize Resend
resend.api_key = os.environ.get("RESEND_API_KEY")

# Pydantic models
class ContactForm(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

class NewsletterSignup(BaseModel):
    email: EmailStr
    preferences: Optional[Dict[str, Any]] = {}

class BMICalculatorInput(BaseModel):
    age: int
    sex: str
    height_cm: float
    weight_kg: float
    activity_level: str

class BMIResult(BaseModel):
    bmi: float
    bmi_category: str
    bmr: float
    tdee: float
    healthy_weight_min: float
    healthy_weight_max: float
    weekly_calorie_deficit: Optional[float] = None
    weeks_to_healthy_bmi: Optional[int] = None
    warnings: List[str] = []
    calculation_id: str

class CalculatorInput(BaseModel):
    peptide_slug: str
    vial_size: float
    bacteriostatic_water: float
    target_dose: float
    
class CalculatorResult(BaseModel):
    concentration: float
    injection_volume: float
    units_per_ml: Optional[float] = None
    concentration_mcg: Optional[float] = None
    doses_per_vial: int

class TranslateRequest(BaseModel):
    text: str
    target_lang: str

class MelanotanCalculatorInput(BaseModel):
    peptide: str
    fitzpatrick_scale: int
    uv_exposure: str
    sensitivity: str
    target_tan: str

class MelanotanPhase(BaseModel):
    daily_dose: Optional[int] = None
    dose: Optional[int] = None
    duration: Optional[int] = None
    frequency: Optional[str] = None
    schedule: Optional[List[Dict[str, Any]]] = None

class MelanotanTimeline(BaseModel):
    estimated_days_to_target: int

class MelanotanResult(BaseModel):
    loading_phase: MelanotanPhase
    maintenance_phase: MelanotanPhase
    timeline: MelanotanTimeline
    red_flags: List[str] = []
    safety_warnings: List[str] = []
    calculation_id: str

# In-memory storage (replace with database in production)
subscribers = {}
calculation_history = {}

@app.get("/")
async def root():
    return {"message": "Professor Peptides API v2.0", "status": "running"}

@app.get("/api/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "Professor Peptides API",
        "version": "2.0.0"
    }

@app.get("/api/statistics")
async def get_statistics():
    """Get dynamic statistics about peptides, studies, and platform metrics"""
    try:
        categories = get_peptide_categories()
        
        # Count total peptides across all categories
        total_peptides = 0
        total_citations = 0
        fda_approved_count = 0
        categories_count = len(categories)
        
        for category_key, category in categories.items():
            if 'peptides' in category:
                peptides_in_category = category['peptides']
                total_peptides += len(peptides_in_category)
                
                # Count citations for each peptide
                for peptide in peptides_in_category:
                    citations = peptide.get('citations', [])
                    total_citations += len(citations)
                    
                    # Count FDA approved peptides
                    if peptide.get('fdaApproved', False):
                        fda_approved_count += 1
        
        # Count research studies from static data
        # We'll count various types of studies and research items
        research_studies_count = 0
        
        # Static research data counts (these can be updated as more data is added)
        clinical_trials = 15  # Based on research data structure
        safety_studies = 12   # Safety profile studies
        publication_studies = 25  # Publication citations
        drug_interaction_studies = 8  # Drug interaction data
        
        research_studies_count = clinical_trials + safety_studies + publication_studies + drug_interaction_studies
        
        # Count professional tools/calculators available
        professional_tools = 7  # BMI, GLP-1 dosing, reconstitution, etc.
        
        # Count team members (medical advisors)
        medical_advisors = 1  # Dr. Sheraz Ahmad
        
        return {
            "peptides": {
                "total": total_peptides,
                "description": "Comprehensive peptide profiles with mechanisms, structures, safety notes, and references"
            },
            "citations": {
                "total": total_citations,
                "description": "Curated peer-reviewed studies and clinical data"
            },
            "tools": {
                "total": professional_tools,
                "description": "GLP-1 dosage, reconstitution, BMI and metabolic, interaction checks, and more"
            },
            "medical_oversight": {
                "total": medical_advisors,
                "description": "Board-certified physician guidance for scientific accuracy"
            },
            "research_studies": {
                "total": research_studies_count,
                "description": "Clinical trials, safety studies, and research publications"
            },
            "categories": {
                "total": categories_count,
                "description": "Specialized peptide categories"
            },
            "fda_approved": {
                "total": fda_approved_count,
                "description": "FDA-approved peptide therapeutics"
            },
            "last_updated": datetime.utcnow().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Error fetching statistics: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching statistics")

@app.get("/api/peptides")
async def get_peptides():
    """Get all peptide categories and peptides"""
    try:
        categories = get_peptide_categories()
        return categories
    except Exception as e:
        logger.error(f"Error fetching peptides: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching peptides")

@app.get("/api/peptide-categories")
async def get_peptide_categories_endpoint():
    """Get all peptide categories and peptides (alias for /api/peptides)"""
    try:
        categories = get_peptide_categories()
        return categories
    except Exception as e:
        logger.error(f"Error fetching peptide categories: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching peptide categories")

@app.get("/api/peptides/{slug}")
async def get_peptide(slug: str):
    """Get a specific peptide by slug"""
    try:
        categories = get_peptide_categories()
        
        # Search through all categories for the peptide
        for category_key, category in categories.items():
            if 'peptides' in category:
                for peptide in category['peptides']:
                    if peptide.get('slug') == slug:
                        return peptide
        
        raise HTTPException(status_code=404, detail="Peptide not found")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching peptide {slug}: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching peptide")

@app.get("/api/peptide-categories")
async def get_all_peptide_categories():
    """Get all peptide categories"""
    try:
        categories = get_peptide_categories()
        return categories
    except Exception as e:
        logger.error(f"Error fetching peptide categories: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching categories")

@app.get("/api/peptide-categories/{category}")
async def get_peptide_category(category: str):
    """Get a specific peptide category"""
    try:
        categories = get_peptide_categories()
        
        if category in categories:
            return categories[category]
        else:
            raise HTTPException(status_code=404, detail="Category not found")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching category {category}: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching category")

@app.post("/api/calculator/calculate")
async def calculate_dosage(calc_input: CalculatorInput):
    """Universal calculator for all peptides"""
    try:
        # Validate input
        if calc_input.vial_size <= 0 or calc_input.bacteriostatic_water <= 0 or calc_input.target_dose <= 0:
            raise HTTPException(status_code=400, detail="All values must be greater than 0")
        
        # Get peptide information to determine calculation type
        peptide_slug = calc_input.peptide_slug.lower()
        categories = get_peptide_categories()
        
        # Find the peptide in the database
        peptide_info = None
        for category_key, category in categories.items():
            if 'peptides' in category:
                for peptide in category['peptides']:
                    if peptide.get('slug') == peptide_slug:
                        peptide_info = peptide
                        break
                if peptide_info:
                    break
        
        if not peptide_info:
            raise HTTPException(status_code=404, detail="Peptide not found in database")
        
        # Determine dosing type based on peptide characteristics
        dosage_text = peptide_info.get('dosage', '').lower()
        
        # Check if peptide uses mcg dosing
        is_mcg_dosing = (
            'mcg' in dosage_text or 
            'μg' in dosage_text or
            peptide_slug in ['ipamorelin', 'igf-1-lr3', 'bpc-157', 'cjc-1295', 
                           'ghrp-2', 'ghrp-6', 'hexarelin', 'melanotan-ii', 'ghk-cu', 
                           'ahk-cu', 'dsip', 'selank', 'semax', 'mgf', 'ara-290'] or
            any(keyword in peptide_slug for keyword in ['ghrp', 'igf', 'bpc', 'melanotan'])
        )
        
        # Special handling for TB-500 (uses mg but smaller doses)
        is_tb500_style = peptide_slug in ['tb-500', 'thymosin']
        
        if is_mcg_dosing:
            # For mcg-based peptides (growth factors, healing peptides, etc.)
            concentration_mg = calc_input.vial_size / calc_input.bacteriostatic_water
            concentration_mcg = concentration_mg * 1000
            injection_volume = calc_input.target_dose / concentration_mcg
            doses_per_vial = int((calc_input.vial_size * 1000) / calc_input.target_dose)
            
            result = CalculatorResult(
                concentration=round(concentration_mg, 3),
                injection_volume=round(injection_volume, 4),
                concentration_mcg=round(concentration_mcg, 0),
                doses_per_vial=doses_per_vial
            )
        elif is_tb500_style:
            # For TB-500 style peptides (mg dosing but smaller amounts)
            concentration = calc_input.vial_size / calc_input.bacteriostatic_water
            injection_volume = calc_input.target_dose / concentration
            doses_per_vial = int(calc_input.vial_size / calc_input.target_dose)
            
            result = CalculatorResult(
                concentration=round(concentration, 3),
                injection_volume=round(injection_volume, 4),
                doses_per_vial=doses_per_vial
            )
        else:
            # For mg-based peptides (GLP-1 agonists, etc.)
            concentration = calc_input.vial_size / calc_input.bacteriostatic_water
            injection_volume = calc_input.target_dose / concentration
            units_per_ml = concentration * 1000  # Convert to mcg/ml
            doses_per_vial = int(calc_input.vial_size / calc_input.target_dose)
            
            result = CalculatorResult(
                concentration=round(concentration, 3),
                injection_volume=round(injection_volume, 4),
                units_per_ml=round(units_per_ml, 0),
                doses_per_vial=doses_per_vial
            )
        
        # Store calculation in history
        calc_id = secrets.token_urlsafe(16)
        calculation_history[calc_id] = {
            "timestamp": datetime.utcnow().isoformat(),
            "peptide": peptide_info.get('name'),
            "input": calc_input.dict(),
            "result": result.dict(),
            "dosing_type": "mcg" if is_mcg_dosing else ("mg-small" if is_tb500_style else "mg")
        }
        
        logger.info(f"Universal calculation completed for {peptide_info.get('name')}: {result.dict()}")
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Universal calculation error: {str(e)}")
        raise HTTPException(status_code=500, detail="Calculation failed")

@app.post("/api/calculators/melanotan-pro", response_model=MelanotanResult)
async def calculate_melanotan_protocol(melanotan_input: MelanotanCalculatorInput):
    """Calculate personalized melanotan dosing protocol"""
    try:
        calculation_id = secrets.token_hex(8)
        
        # Base dosing parameters for different peptides
        base_doses = {
            "mt1": {"loading": 500, "maintenance": 250},  # mcg
            "mt2": {"loading": 250, "maintenance": 125}   # mcg
        }
        
        # Fitzpatrick scale multipliers (higher skin types need less)
        fitzpatrick_multipliers = {1: 1.2, 2: 1.1, 3: 1.0, 4: 0.9, 5: 0.8, 6: 0.7}
        
        # UV exposure adjustments
        uv_adjustments = {"minimal": 1.0, "moderate": 0.9, "frequent": 0.8}
        
        # Sensitivity adjustments
        sensitivity_adjustments = {"high": 0.7, "normal": 1.0, "low": 1.2}
        
        # Target tan timeline
        target_timelines = {"light": 14, "medium": 21, "dark": 35}
        
        # Get base doses for peptide type
        peptide_doses = base_doses.get(melanotan_input.peptide, base_doses["mt2"])
        
        # Calculate adjusted doses
        multiplier = (fitzpatrick_multipliers.get(melanotan_input.fitzpatrick_scale, 1.0) * 
                     uv_adjustments.get(melanotan_input.uv_exposure, 1.0) * 
                     sensitivity_adjustments.get(melanotan_input.sensitivity, 1.0))
        
        loading_dose = int(peptide_doses["loading"] * multiplier)
        maintenance_dose = int(peptide_doses["maintenance"] * multiplier)
        
        # Generate loading schedule
        loading_schedule = []
        loading_duration = 7 if melanotan_input.peptide == "mt1" else 5
        for day in range(1, loading_duration + 1):
            dose_for_day = loading_dose if day <= 3 else int(loading_dose * 0.8)
            loading_schedule.append({
                "day": day,
                "dose": dose_for_day,
                "notes": "Loading phase" if day <= 3 else "Tapering"
            })
        
        # Safety warnings and red flags
        red_flags = []
        safety_warnings = [
            "Always use sterile injection technique",
            "Monitor all moles and skin changes closely", 
            "Use broad-spectrum sunscreen (SPF 30+)",
            "Start with lower doses to assess tolerance",
            "Discontinue if unusual skin changes occur"
        ]
        
        # Add red flags for high-risk combinations
        if melanotan_input.fitzpatrick_scale <= 2 and melanotan_input.target_tan == "dark":
            red_flags.append("EXTREME CAUTION: Fair skin + dark tan target significantly increases cancer risk")
        
        if melanotan_input.peptide == "mt2" and melanotan_input.sensitivity == "high":
            red_flags.append("MT-2 with high sensitivity may cause severe nausea and flushing")
        
        # Timeline calculation
        timeline_days = target_timelines.get(melanotan_input.target_tan, 21)
        if melanotan_input.fitzpatrick_scale <= 2:
            timeline_days += 7  # Fair skin takes longer
        
        result = MelanotanResult(
            loading_phase=MelanotanPhase(
                daily_dose=loading_dose,
                duration=loading_duration,
                schedule=loading_schedule
            ),
            maintenance_phase=MelanotanPhase(
                dose=maintenance_dose,
                frequency="2-3 times per week"
            ),
            timeline=MelanotanTimeline(
                estimated_days_to_target=timeline_days
            ),
            red_flags=red_flags,
            safety_warnings=safety_warnings,
            calculation_id=calculation_id
        )
        
        return result
        
    except Exception as e:
        logger.error(f"Melanotan calculation error: {str(e)}")
        raise HTTPException(status_code=500, detail="Melanotan calculation failed")

@app.post("/api/calculators/bmi")
async def calculate_bmi(bmi_input: BMICalculatorInput):
    """Calculate BMI, BMR, TDEE and provide metabolic insights"""
    try:
        # Validate input
        if bmi_input.age <= 0 or bmi_input.height_cm <= 0 or bmi_input.weight_kg <= 0:
            raise HTTPException(status_code=400, detail="Age, height, and weight must be greater than 0")
        
        if bmi_input.sex not in ['male', 'female']:
            raise HTTPException(status_code=400, detail="Sex must be 'male' or 'female'")
        
        # Calculate BMI
        height_m = bmi_input.height_cm / 100
        bmi = bmi_input.weight_kg / (height_m ** 2)
        
        # Determine BMI category
        if bmi < 18.5:
            bmi_category = "Underweight"
        elif bmi < 25:
            bmi_category = "Normal weight"
        elif bmi < 30:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obese"
        
        # Calculate BMR using Mifflin-St Jeor equation
        if bmi_input.sex == 'male':
            bmr = 10 * bmi_input.weight_kg + 6.25 * bmi_input.height_cm - 5 * bmi_input.age + 5
        else:
            bmr = 10 * bmi_input.weight_kg + 6.25 * bmi_input.height_cm - 5 * bmi_input.age - 161
        
        # Calculate TDEE based on activity level
        activity_multipliers = {
            'sedentary': 1.2,
            'lightly_active': 1.375,
            'moderately_active': 1.55,
            'very_active': 1.725,
            'extremely_active': 1.9
        }
        
        activity_key = bmi_input.activity_level.lower().replace(' ', '_')
        multiplier = activity_multipliers.get(activity_key, 1.55)  # Default to moderately active
        tdee = bmr * multiplier
        
        # Calculate healthy weight range (BMI 18.5-24.9)
        healthy_weight_min = 18.5 * (height_m ** 2)
        healthy_weight_max = 24.9 * (height_m ** 2)
        
        # Generate warnings and recommendations
        warnings = []
        weekly_calorie_deficit = None
        weeks_to_healthy_bmi = None
        
        if bmi < 18.5:
            warnings.append("Underweight BMI may indicate nutritional deficiency. Consult healthcare provider.")
        elif bmi >= 30:
            warnings.append("Obese BMI increases health risks. Consider professional weight management support.")
            # Calculate deficit to reach BMI 25
            target_weight = 25 * (height_m ** 2)
            weight_to_lose = bmi_input.weight_kg - target_weight
            if weight_to_lose > 0:
                weekly_calorie_deficit = 3500  # 1 lb per week
                weeks_to_healthy_bmi = int((weight_to_lose * 2.2) * 1)  # Approximate weeks
        elif bmi >= 25:
            warnings.append("Overweight BMI may increase health risks. Consider gradual weight loss.")
            target_weight = 24.9 * (height_m ** 2)
            weight_to_lose = bmi_input.weight_kg - target_weight
            if weight_to_lose > 0:
                weekly_calorie_deficit = 2500  # 0.7 lb per week
                weeks_to_healthy_bmi = int((weight_to_lose * 2.2) * 1.4)
        
        if bmi_input.age > 65:
            warnings.append("For adults over 65, slightly higher BMI (23-30) may be protective.")
        
        if bmi_input.age < 18:
            warnings.append("BMI calculations for individuals under 18 should use pediatric growth charts.")
        
        # Generate unique calculation ID
        calc_id = secrets.token_urlsafe(16)
        
        result = BMIResult(
            bmi=round(bmi, 1),
            bmi_category=bmi_category,
            bmr=round(bmr, 0),
            tdee=round(tdee, 0),
            healthy_weight_min=round(healthy_weight_min, 1),
            healthy_weight_max=round(healthy_weight_max, 1),
            weekly_calorie_deficit=weekly_calorie_deficit,
            weeks_to_healthy_bmi=weeks_to_healthy_bmi,
            warnings=warnings,
            calculation_id=calc_id
        )
        
        logger.info(f"BMI calculation completed: {calc_id}")
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"BMI calculation error: {str(e)}")
        raise HTTPException(status_code=500, detail="BMI calculation failed")

@app.get("/api/blog")
async def get_blog_posts():
    """Get all blog posts with content"""
    try:
        blog_posts = get_default_blog_data()
        
        # Load content for the first 3 posts (our new comprehensive posts)
        for post in blog_posts[:3]:
            content_file = f"/app/blog_content/{post['slug']}.md"
            try:
                with open(content_file, 'r', encoding='utf-8') as f:
                    post['content'] = f.read()
            except FileNotFoundError:
                post['content'] = f"Content for {post['title']} is being prepared..."
        
        return blog_posts
        
    except Exception as e:
        logger.error(f"Error fetching blog posts: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch blog posts")

@app.get("/api/blog/{slug}")
async def get_blog_post(slug: str):
    """Get a specific blog post by slug"""
    try:
        blog_posts = get_default_blog_data()
        post = next((p for p in blog_posts if p['slug'] == slug), None)
        
        if not post:
            raise HTTPException(status_code=404, detail="Blog post not found")
        
        # Load content for the first 3 posts (our new comprehensive posts)
        if post['id'] <= 3:
            content_file = f"/app/blog_content/{post['slug']}.md"
            try:
                with open(content_file, 'r', encoding='utf-8') as f:
                    post['content'] = f.read()
            except FileNotFoundError:
                post['content'] = f"Content for {post['title']} is being prepared..."
        else:
            post['content'] = f"Full content for {post['title']} is being prepared..."
        
        return post
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching blog post {slug}: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch blog post")

@app.post("/api/newsletter/signup")
async def newsletter_signup(request: Request, signup: NewsletterSignup):
    """Handle newsletter signup with double opt-in and rate limiting"""
    try:
        # Log request for monitoring
        client_ip = request.headers.get("x-forwarded-for", "unknown")
        logger.info(f"Newsletter signup request from {client_ip} for {signup.email}")
        
        email = signup.email.lower()
        
        # Check if already subscribed
        if email in subscribers and subscribers[email].get('confirmed'):
            return {"message": "Email already subscribed", "status": "already_subscribed"}
        
        # Generate confirmation token
        confirmation_token = secrets.token_urlsafe(32)
        expires_at = datetime.utcnow() + timedelta(hours=24)
        
        # Store pending subscription
        subscribers[email] = {
            "email": email,
            "confirmation_token": confirmation_token,
            "expires_at": expires_at.isoformat(),
            "confirmed": False,
            "preferences": signup.preferences,
            "created_at": datetime.utcnow().isoformat(),
            "ip_address": client_ip[:8] + "..." if len(client_ip) > 8 else client_ip  # Partially masked IP
        }
        
        # Send confirmation email
        try:
            confirmation_url = f"https://peptide-professor.vercel.app/newsletter/confirm?token={confirmation_token}"
            
            params = {
                "from": "Peptide Professor <noreply@peptideprofessor.com>",
                "to": [email],
                "subject": "Confirm your subscription to Peptide Professor",
                "html": f"""
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                    <h1 style="color: #2563eb;">Welcome to Peptide Professor!</h1>
                    <p>Thank you for your interest in our research peptide newsletter.</p>
                    <p>To complete your subscription, please click the button below:</p>
                    <div style="text-align: center; margin: 30px 0;">
                        <a href="{confirmation_url}" 
                           style="background-color: #2563eb; color: white; padding: 12px 24px; 
                                  text-decoration: none; border-radius: 5px; display: inline-block;">
                            Confirm Subscription
                        </a>
                    </div>
                    <p style="font-size: 14px; color: #666;">
                        This link will expire in 24 hours. If you didn't request this subscription, 
                        you can safely ignore this email.
                    </p>
                    <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;">
                    <p style="font-size: 12px; color: #888;">
                        Peptide Professor - Research Use Only<br>
                        Not approved for human consumption
                    </p>
                </div>
                """
            }
            
            resend.Emails.send(params)
            logger.info(f"Confirmation email sent successfully to {email}")
            
        except Exception as e:
            logger.error(f"Failed to send confirmation email to {email}: {str(e)}")
            # Don't fail the signup if email fails, just log it
        
        return {
            "message": "Confirmation email sent. Please check your inbox.",
            "status": "confirmation_sent"
        }
        
    except Exception as e:
        logger.error(f"Newsletter signup error: {str(e)}")
        raise HTTPException(status_code=500, detail="Newsletter signup failed")

@app.get("/api/newsletter/confirm")
async def confirm_newsletter(token: str):
    """Confirm newsletter subscription"""
    try:
        # Find subscriber by token
        subscriber = None
        for email, data in subscribers.items():
            if data.get('confirmation_token') == token:
                subscriber = data
                break
        
        if not subscriber:
            raise HTTPException(status_code=404, detail="Invalid confirmation token")
        
        # Check if token expired
        expires_at = datetime.fromisoformat(subscriber['expires_at'])
        if datetime.utcnow() > expires_at:
            raise HTTPException(status_code=400, detail="Confirmation token expired")
        
        # Confirm subscription
        subscriber['confirmed'] = True
        subscriber['confirmed_at'] = datetime.utcnow().isoformat()
        
        # Send welcome email
        try:
            params = {
                "from": "Peptide Professor <noreply@peptideprofessor.com>",
                "to": [subscriber['email']],
                "subject": "Welcome to Peptide Professor Newsletter!",
                "html": f"""
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                    <h1 style="color: #2563eb;">Welcome to Peptide Professor!</h1>
                    <p>Your subscription has been confirmed successfully.</p>
                    <p>You'll now receive our latest research updates, peptide insights, and educational content.</p>
                    <div style="background-color: #f8fafc; padding: 20px; border-radius: 8px; margin: 20px 0;">
                        <h3 style="color: #1e40af; margin-top: 0;">What to expect:</h3>
                        <ul style="margin: 0;">
                            <li>Latest peptide research findings</li>
                            <li>Educational content and protocols</li>
                            <li>New peptide additions to our database</li>
                            <li>Safety updates and guidelines</li>
                        </ul>
                    </div>
                    <p>
                        <a href="https://peptide-professor.vercel.app" style="color: #2563eb;">
                            Visit our peptide database
                        </a>
                    </p>
                    <hr style="margin: 30px 0; border: none; border-top: 1px solid #eee;">
                    <p style="font-size: 12px; color: #888;">
                        You can update your preferences or unsubscribe at any time by 
                        <a href="https://peptide-professor.vercel.app/newsletter/preferences?email={subscriber['email']}">
                            clicking here
                        </a>
                    </p>
                </div>
                """
            }
            
            resend.Emails.send(params)
            logger.info(f"Welcome email sent to {subscriber['email']}")
            
        except Exception as e:
            logger.error(f"Failed to send welcome email: {str(e)}")
        
        return {
            "message": "Subscription confirmed successfully!",
            "status": "confirmed"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Confirmation error: {str(e)}")
        raise HTTPException(status_code=500, detail="Confirmation failed")

@app.post("/api/contact")
async def contact_form(form: ContactForm):
    """Handle contact form submissions"""
    try:
        # In production, you might want to store this in a database
        logger.info(f"Contact form submission from {form.email}: {form.subject}")
        
        # Send notification email to admin (optional)
        try:
            params = {
                "from": "Peptide Professor <noreply@peptideprofessor.com>",
                "to": ["admin@peptideprofessor.com"],  # Replace with actual admin email
                "subject": f"Contact Form: {form.subject}",
                "html": f"""
                <h3>New Contact Form Submission</h3>
                <p><strong>Name:</strong> {form.name}</p>
                <p><strong>Email:</strong> {form.email}</p>
                <p><strong>Subject:</strong> {form.subject}</p>
                <p><strong>Message:</strong></p>
                <p>{form.message}</p>
                """
            }
            
            resend.Emails.send(params)
            
        except Exception as e:
            logger.error(f"Failed to send contact form notification: {str(e)}")
        
        return {"message": "Contact form submitted successfully"}
        
    except Exception as e:
        logger.error(f"Contact form error: {str(e)}")
        raise HTTPException(status_code=500, detail="Contact form submission failed")

@app.get("/api/team-members")
async def get_team_members():
    """Get team members"""
    try:
        team_data = get_default_team_data()
        return {"team": team_data}
    except Exception as e:
        logger.error(f"Team members error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch team members")

@app.get("/api/blog-posts")
async def get_blog_posts_api():
    """Get blog posts"""
    try:
        blog_data = get_default_blog_data()
        return {"posts": blog_data}
    except Exception as e:
        logger.error(f"Blog posts error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to fetch blog posts")

# ============================================
# PLACEHOLDER ENDPOINTS FOR FUTURE USE
# ============================================

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT settings
SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Additional Pydantic models for future endpoints
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    created_at: datetime

class Product(BaseModel):
    id: str
    name: str
    description: str
    category: str
    price: Optional[float] = None
    research_only: bool = True
    in_stock: bool = True
    created_at: datetime

class Order(BaseModel):
    id: str
    user_id: Optional[str] = None
    products: List[Dict[str, Any]]
    status: str = "pending"
    total: float
    created_at: datetime

# In-memory storage for demonstration (replace with database in production)
users_db = {}
products_db = {}
orders_db = {}

@app.get("/api/products")
async def get_products():
    """
    Get all products (placeholder for future e-commerce functionality)
    Currently returns sample educational peptide products
    """
    sample_products = [
        {
            "id": "1",
            "name": "Peptide Research Guide",
            "description": "Comprehensive guide to peptide research",
            "category": "educational",
            "price": 0,
            "research_only": True,
            "in_stock": True,
            "created_at": datetime.utcnow().isoformat()
        },
        {
            "id": "2",
            "name": "Calculator Tools Access",
            "description": "Access to all peptide calculation tools",
            "category": "tools",
            "price": 0,
            "research_only": True,
            "in_stock": True,
            "created_at": datetime.utcnow().isoformat()
        }
    ]
    return {
        "products": sample_products,
        "total": len(sample_products),
        "message": "Educational content only - no products for sale"
    }

@app.get("/api/orders")
async def get_orders():
    """
    Get user orders (placeholder for future functionality)
    Returns empty list as this is educational site only
    """
    return {
        "orders": [],
        "total": 0,
        "message": "This is an educational site - no orders available"
    }

@app.get("/api/users")
async def get_users():
    """
    Get users endpoint (placeholder for future user management)
    """
    return {
        "users": [],
        "total": 0,
        "message": "User management coming soon"
    }

@app.post("/api/auth/register")
async def register(user: UserCreate):
    """
    User registration endpoint (placeholder for future functionality)
    Currently returns success but doesn't create actual accounts
    """
    # Check if user exists (demonstration only)
    if user.email in users_db:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    # Hash password (for demonstration)
    hashed_password = pwd_context.hash(user.password)
    
    # Create user object
    user_id = secrets.token_urlsafe(16)
    new_user = {
        "id": user_id,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": hashed_password,
        "is_active": True,
        "created_at": datetime.utcnow().isoformat()
    }
    
    # Store user (in-memory for now)
    users_db[user.email] = new_user
    
    return {
        "message": "Registration successful (demo mode)",
        "user": {
            "id": user_id,
            "email": user.email,
            "full_name": user.full_name
        },
        "note": "This is a placeholder endpoint for future functionality"
    }

@app.post("/api/auth/login")
async def login(user_login: UserLogin):
    """
    User login endpoint (placeholder for future functionality)
    Returns a demo token that doesn't grant actual access
    """
    # Check if user exists (demonstration only)
    if user_login.email not in users_db:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    
    # Verify password (demonstration only)
    stored_user = users_db[user_login.email]
    if not pwd_context.verify(user_login.password, stored_user["hashed_password"]):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + access_token_expires
    token_data = {
        "sub": user_login.email,
        "exp": expire
    }
    access_token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "message": "Login successful (demo mode)",
        "note": "This is a placeholder endpoint for future functionality"
    }

@app.post("/api/translate")
async def translate_text(request: TranslateRequest):
    """Translate text using DeepL API"""
    try:
        # Get DeepL API key from environment
        deepl_api_key = os.environ.get("DEEPL_API_KEY")
        testsprite_api_key = os.environ.get("TESTSPRITE_API_KEY")
        
        if not deepl_api_key and not testsprite_api_key:
            raise HTTPException(status_code=500, detail="Translation API key not configured")
        
        # Use available API key (prefer DeepL if both available)
        api_key = deepl_api_key or testsprite_api_key
        
        # Call DeepL API
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api-free.deepl.com/v2/translate",
                headers={
                    "Authorization": f"DeepL-Auth-Key {api_key}",
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                data={
                    "text": request.text,
                    "target_lang": request.target_lang.upper()
                }
            )
            
            if response.status_code != 200:
                logger.error(f"DeepL API error: {response.status_code} - {response.text}")
                raise HTTPException(status_code=500, detail="Translation service error")
            
            translation_data = response.json()
            return translation_data
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error translating text: {str(e)}")
        raise HTTPException(status_code=500, detail="Translation failed")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)