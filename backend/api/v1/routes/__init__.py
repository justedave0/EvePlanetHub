from fastapi import APIRouter
from . import health
from . import auth

router = APIRouter()

# Include all route modules
router.include_router(health.router, prefix="/health")
router.include_router(auth.router, prefix="/auth", tags=["Authentication"])