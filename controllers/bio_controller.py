from services.bio_service import generate_ai_bios
from schemas.bio_schema import BioRequest, BioResponse
from fastapi import HTTPException

def generate_bios_controller(request: BioRequest) -> BioResponse:
    try:
        bios = generate_ai_bios(request.about_me)
        return BioResponse(bios=bios)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
