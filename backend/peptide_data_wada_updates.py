# Add new peptides and WADA status updates

# First, let's add the missing WADA banned peptides that we identified

hgh_peptide = {
    "name": "HGH (Human Growth Hormone)", 
    "slug": "hgh",
    "fdaApproved": True,
    "wadaBanned": True,
    "approvedFor": ["Growth hormone deficiency", "Turner syndrome", "Chronic kidney disease"],
    "description": "Human Growth Hormone (HGH) is a naturally occurring hormone produced by the pituitary gland that stimulates growth, cell reproduction, and regeneration in humans. FDA-approved for specific medical conditions including growth hormone deficiency in children and adults. HGH has been extensively studied for its effects on muscle mass, bone density, metabolism, and overall body composition. Due to its performance-enhancing properties, it is banned by WADA for competitive athletes.",
    "benefits": ["Increased muscle mass", "Reduced body fat", "Enhanced bone density", "Improved exercise capacity", "Anti-aging effects", "Better sleep quality"],
    "dosage": "Medical use: 0.15-0.3mg daily | Research protocols: 1-4 IU daily depending on goals",
    "mechanism": "Directly stimulates protein synthesis, lipolysis, and gluconeogenesis through IGF-1 mediated pathways",
    "sideEffects": ["Joint pain", "Muscle pain", "Fluid retention", "Carpal tunnel syndrome", "Increased insulin resistance"],
    "contraindications": ["Active malignancy", "Diabetic retinopathy", "Acute critical illness"],
    "athleteWarning": "🛑 WADA BANNED - Strictly prohibited in competitive sports at all times"
}

mgf_peptide = {
    "name": "MGF (Mechano Growth Factor)", 
    "slug": "mgf",
    "fdaApproved": False,
    "wadaBanned": True,
    "researchStatus": "Research compound - IGF-1 splice variant",
    "description": "Mechano Growth Factor (MGF) is a splice variant of IGF-1 that is produced in response to muscle damage or stress. This peptide plays a crucial role in muscle repair and hypertrophy by activating satellite cells and promoting muscle fiber regeneration. MGF is released locally in muscle tissue following mechanical stress, making it a key factor in exercise-induced muscle adaptation. Research suggests it may be more potent than IGF-1 for muscle growth and repair.",
    "benefits": ["Muscle growth and repair", "Enhanced recovery", "Satellite cell activation", "Improved muscle fiber regeneration", "Post-workout recovery", "Strength gains"],
    "dosage": "Research protocols: 200-400mcg subQ post-workout, site-specific injection",
    "mechanism": "Activates satellite cells and stimulates muscle protein synthesis through IGF-1 receptor pathway",
    "researchFindings": ["Enhanced muscle repair in animal studies", "Improved muscle fiber regeneration", "Increased satellite cell activation", "Superior muscle growth compared to regular IGF-1"],
    "safetyNote": "Research compound only. Limited human safety data available.",
    "athleteWarning": "🛑 WADA BANNED - Prohibited in competitive sports as growth factor"
}

selank_peptide = {
    "name": "Selank", 
    "slug": "selank",
    "fdaApproved": False,
    "wadaBanned": True,
    "researchStatus": "Research compound - Nootropic peptide",
    "description": "Selank is a synthetic heptapeptide derived from tuftsin, a natural immunomodulatory peptide. Originally developed in Russia, Selank has been studied for its anxiolytic, nootropic, and immunomodulatory properties. It works by influencing GABA, serotonin, and dopamine neurotransmitter systems while also affecting the expression of brain-derived neurotrophic factor (BDNF). Research suggests it may help with anxiety, depression, cognitive function, and stress resilience without the side effects of traditional anxiolytics.",
    "benefits": ["Anxiety reduction", "Cognitive enhancement", "Stress resilience", "Mood improvement", "Memory enhancement", "Immune system support"],
    "dosage": "Research protocols: 250-500mcg daily, available as nasal spray or subcutaneous injection",
    "mechanism": "Modulates GABA, serotonin, and dopamine while increasing BDNF expression for neuroprotection",
    "researchFindings": ["Reduced anxiety in clinical studies", "Improved cognitive performance", "Enhanced stress tolerance", "Neuroprotective effects"],
    "safetyNote": "Research compound with limited long-term safety data in humans.",
    "athleteWarning": "🛑 WADA BANNED - Prohibited as cognitive enhancer that may provide unfair advantage"
}

ara290_peptide = {
    "name": "ARA-290 (Cibinetide)", 
    "slug": "ara-290",
    "fdaApproved": False,
    "wadaBanned": False,
    "researchStatus": "Research compound - Erythropoietin receptor agonist",
    "description": "ARA-290, also known as Cibinetide, is a synthetic peptide derived from erythropoietin that selectively activates the innate repair receptor (IRR) without stimulating red blood cell production. It was originally developed for treating diabetic neuropathy and has shown promise in various neuroprotective and tissue repair applications. Unlike EPO, ARA-290 does not increase hematocrit, making it potentially safer for therapeutic use while retaining tissue-protective properties.",
    "benefits": ["Neuroprotection", "Nerve repair", "Pain reduction", "Inflammation control", "Tissue healing", "Diabetic neuropathy support"],
    "dosage": "Research protocols: 2-4mg subcutaneous daily for 28 days",
    "mechanism": "Activates innate repair receptor (IRR) to promote tissue protection and repair without hematopoietic effects",
    "researchFindings": ["Improved nerve function in diabetic neuropathy", "Reduced neuropathic pain", "Enhanced tissue repair", "Anti-inflammatory effects"],
    "safetyNote": "Research compound with ongoing clinical trials. Generally well-tolerated in studies.",
    "athleteWarning": "Not WADA banned - currently not prohibited for competitive athletes"
}

# New emerging peptides from the tool data
slu_pp332_peptide = {
    "name": "SLU PP 332", 
    "slug": "slu-pp-332",
    "fdaApproved": False,
    "wadaBanned": False,
    "researchStatus": "Research compound - Exercise mimetic",
    "description": "SLU PP 332 is an experimental exercise mimetic peptide that activates similar pathways to physical exercise without the need for actual exercise. This compound is designed to activate AMPK (AMP-activated protein kinase) and ERR (estrogen-related receptor) pathways, which are crucial for energy metabolism, mitochondrial biogenesis, and fat oxidation. It represents a new frontier in metabolic research, potentially offering benefits of exercise training for those unable to exercise traditionally.",
    "benefits": ["Exercise mimetic effects", "Enhanced endurance", "Fat burning", "Metabolic activation", "Mitochondrial biogenesis", "Energy enhancement"],
    "dosage": "Research protocols under development - dosage not yet established",
    "mechanism": "Activates AMPK and ERR pathways to mimic exercise-induced metabolic changes",
    "researchFindings": ["Mimics exercise benefits in preclinical studies", "Enhanced fat oxidation", "Improved metabolic parameters", "Increased mitochondrial activity"],
    "safetyNote": "Early-stage research compound. Safety profile under investigation.",
    "athleteWarning": "Not currently WADA banned but may be evaluated as research progresses"
}

ahk_cu_peptide = {
    "name": "AHK-Cu (Copper Peptide)", 
    "slug": "ahk-cu",
    "fdaApproved": False,
    "wadaBanned": False,
    "researchStatus": "Research compound - Copper-binding peptide",
    "description": "AHK-Cu is a copper-binding peptide complex that has gained attention for its potential hair growth and skin repair properties. This tripeptide (Ala-His-Lys) bound to copper has been studied for its ability to stimulate hair follicles, promote wound healing, and enhance collagen production. It's commonly used in cosmeceutical applications and is considered a safer alternative to more potent copper peptides like GHK-Cu for topical applications.",
    "benefits": ["Hair growth stimulation", "Skin repair", "Collagen production", "Wound healing", "Anti-aging effects", "Follicle stimulation"],
    "dosage": "Research protocols: 0.5-1mg subcutaneous daily or topical application",
    "mechanism": "Copper-peptide complex that stimulates cellular repair processes and collagen synthesis",
    "researchFindings": ["Enhanced hair growth in studies", "Improved skin texture and elasticity", "Accelerated wound healing", "Increased collagen production"],
    "safetyNote": "Generally well-tolerated with minimal side effects reported.",
    "athleteWarning": "Not WADA banned - safe for competitive athletes"
}

thymulin_peptide = {
    "name": "Thymulin", 
    "slug": "thymulin",
    "fdaApproved": False,
    "wadaBanned": False,
    "researchStatus": "Research compound - Thymic hormone",
    "description": "Thymulin is a nonapeptide hormone naturally produced by the thymus gland that plays a crucial role in immune system regulation and T-cell maturation. As we age, thymus function and thymulin production decline, leading to compromised immune function. Synthetic thymulin has been studied for its ability to restore immune function, reduce inflammation, and support healthy aging by maintaining proper T-cell balance and immune system homeostasis.",
    "benefits": ["Immune system regulation", "T-cell maturation", "Anti-inflammatory effects", "Anti-aging support", "Allergy reduction", "Immune homeostasis"],
    "dosage": "Research protocols: 1-2mg subcutaneous 2-3 times weekly",
    "mechanism": "Regulates T-helper cell balance and supports thymic function for optimal immune response",
    "researchFindings": ["Improved immune function in aging", "Reduced allergic responses", "Enhanced T-cell activity", "Anti-inflammatory benefits"],
    "safetyNote": "Research compound with good safety profile in preliminary studies.",
    "athleteWarning": "Not WADA banned - may actually support athlete health and recovery"
}

# WADA status updates for existing peptides - these need to be applied to the main peptide_data.py file
wada_updates = {
    # Already updated: Semaglutide (False), Tirzepatide (False), AOD9604 (True)
    "bpc-157": True,
    "tb-500": True,
    "cjc-1295": True,
    "ghrp-2": True,
    "ghrp-6": True,
    "ghk-cu": True,
    "hexarelin": True,
    "igf-1-lr3": True,
    "ipamorelin": True,
    "ll-37": True,
    "thymosin-alpha-1": True,
    # Non-banned peptides
    "tesamorelin": False,
    "5-amino-1mq": False,
    "adipotide": False,
    "cagrilintide": False,
    "mazdutide": False,
    "survodutide": False,
    "retatrutide": False,
    "l-carnitine": False,
    "lipo-c-formula": False,
    "super-mic": False,
    "mots-c": False,
    "epithalon": False,
    "nad-plus": False,
    "glutathione": False,
    "dsip": False,
    "semax": False,
    "kpv": False,
    "vip": False,
    "pt-141": False,
    "oxytocin": False,
    "kisspeptin": False,
    "melanotan-1": False,
    "melanotan-2": False
}