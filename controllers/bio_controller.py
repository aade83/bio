from services.bio_service import generate_ai_bio
from schemas.bio_schema import BioRequest, BioResponse
from fastapi import HTTPException

def generate_bio_controller(request: BioRequest) -> BioResponse:
    try:
        bios = generate_ai_bio(request.text)
        return BioResponse(status="success", message="Bio generated successfully", data=bios)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))# Updated script
