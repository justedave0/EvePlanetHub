from fastapi import APIRouter
from . import health

router = APIRouter()

# Include all route modules
router.include_router(health.router, prefix="/health")