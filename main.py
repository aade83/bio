from fastapi import FastAPI
from routes.bio_routes import router as bio_router

app = FastAPI()
app.include_router(bio_router)
