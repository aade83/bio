from fastapi import APIRouter
from controllers.bio_controller import generate_bio_controller
from schemas.bio_schema import BioRequest, BioResponse

router = APIRouter()

@router.post("/generate-bio", response_model=BioResponse)
def generate_bio(request: BioRequest):
    return generate_bio_controller(request)
# Updated script
