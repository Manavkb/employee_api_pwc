"""routers/health.py - operational endpoints (no API version prefix)."""
from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check():
    return {"status": "healthy",
            "version": settings.VERSION,
            "environment": settings.ENVIRONMENT}
