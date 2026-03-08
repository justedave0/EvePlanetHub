from fastapi import APIRouter
from . import eve

router = APIRouter()
router.include_router(eve.router, prefix="/eve", tags=["EVE Authentication"])