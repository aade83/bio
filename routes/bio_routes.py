from fastapi import APIRouter, Depends
from controllers.bio_controller import generate_bios_controller
from schemas.bio_schema import BioRequest, BioResponse

router = APIRouter()

@router.post("/generate-bios", response_model=BioResponse)
def generate_bios(request: BioRequest):
    return generate_bios_controller(request)
