from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routes.health import router as health_router
from api.v1.routes.users import router as users_router
from api.v1.routes.auth import router as auth_router
import asyncio

app = FastAPI(
    title="EvePlanetHub API",
    description="A modern web application built with FastAPI backend and React frontend",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router, prefix="/api/v1/health", tags=["Health"])
app.include_router(users_router, prefix="/api/v1/users", tags=["Users"])
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])

@app.get("/")
async def root():
    return {"message": "Welcome to EvePlanetHub API"}

# Remove the startup event - let's use a more robust approach by
# using an external startup script with retry logic