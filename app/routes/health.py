from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_checker():
    """Health checker endpoint"""
    return {"success": True}
