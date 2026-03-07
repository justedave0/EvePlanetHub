from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routes.health import router as health_router
from api.v1.routes.users import router as users_router
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

@app.get("/")
async def root():
    return {"message": "Welcome to EvePlanetHub API"}

# Simplify the startup event to only check connection 
@app.on_event("startup")
async def startup_event():
    """Simple startup - just verify database connection works"""
    try:
        from src.database.session import engine
        from sqlalchemy import text
        
        print("Starting application...")
        
        # Simple database connection check
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
            
        print("Database connection successful!")
        print("Application started successfully!") 
        
    except Exception as e:
        print(f"Failed to initialize application: {e}")
        raise

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)