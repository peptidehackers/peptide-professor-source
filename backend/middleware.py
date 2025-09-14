"""
Rate limiting and CORS middleware for Peptide Professor API
"""
import time
import os
from collections import defaultdict
from fastapi import Request
from fastapi.responses import JSONResponse
from typing import Dict

# Simple in-memory rate limiter
class RateLimiter:
    def __init__(self):
        self.requests: Dict[str, list] = defaultdict(list)
        self.window_size = 60  # 60 seconds
        self.max_requests = 60  # 60 requests per minute
    
    def is_allowed(self, identifier: str) -> bool:
        now = time.time()
        # Clean old requests
        self.requests[identifier] = [
            req_time for req_time in self.requests[identifier] 
            if now - req_time < self.window_size
        ]
        
        # Check if under limit
        if len(self.requests[identifier]) < self.max_requests:
            self.requests[identifier].append(now)
            return True
        return False

rate_limiter = RateLimiter()

async def rate_limit_middleware(request: Request, call_next):
    """Rate limiting middleware"""
    if request.url.path.startswith("/api/"):
        # Get client IP
        client_ip = request.headers.get("x-forwarded-for", "").split(",")[0].strip()
        if not client_ip:
            client_ip = request.headers.get("x-real-ip", "")
        if not client_ip:
            client_ip = "unknown"
        
        # Apply rate limiting to POST endpoints
        if request.method == "POST":
            if not rate_limiter.is_allowed(client_ip):
                return JSONResponse(
                    status_code=429,
                    content={"detail": "Too Many Requests"}
                )
    
    response = await call_next(request)
    return response

def validate_cors_origin(origin: str) -> bool:
    """Validate CORS origin against allowed domains"""
    # Read allowed origins from environment variable
    allowed_origins_env = os.environ.get("ALLOWED_ORIGINS", "")
    if allowed_origins_env:
        allowed_origins = [origin.strip() for origin in allowed_origins_env.split(",")]
    else:
        # Fallback to default allowed origins
        allowed_origins = [
            "https://peptide-professor.vercel.app",
            "https://www.professorpeptides.org",
            "http://localhost:3000",  # Development
        ]
    
    # Allow Vercel preview domains and Replit domains
    if (origin.endswith(".vercel.app") or 
        origin.endswith(".preview.emergentagent.com") or
        origin.endswith(".replit.dev") or
        origin.endswith(".janeway.replit.dev")):
        return True
    
    return origin in allowed_origins

async def cors_middleware(request: Request, call_next):
    """CORS middleware with strict origin validation"""
    origin = request.headers.get("origin", "")
    
    # Handle preflight requests
    if request.method == "OPTIONS":
        if validate_cors_origin(origin):
            response = JSONResponse(content=None, status_code=204)
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
            response.headers["Access-Control-Max-Age"] = "86400"
            return response
        else:
            return JSONResponse(status_code=403, content={"detail": "Forbidden"})
    
    response = await call_next(request)
    
    # Add CORS headers for valid origins
    if validate_cors_origin(origin):
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Credentials"] = "false"
    
    return response