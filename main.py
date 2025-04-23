from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from blueprint_utils import get_astrology_data, get_blueprint_keys

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to Webador if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserData(BaseModel):
    name: str
    email: str
    date_of_birth: str
    time_of_birth: str
    place_of_birth: str
    latitude: float
    longitude: float

@app.post("/soul-blueprint")
async def generate_blueprint(user: UserData):
    astro_data = get_astrology_data(
        name=user.name,
        birthdate=user.date_of_birth,
        birthtime=user.time_of_birth,
        birthplace=user.place_of_birth,
        latitude=user.latitude,
        longitude=user.longitude
    )

    if "error" in astro_data:
        return {"error": astro_data["error"]}

    blueprint = get_blueprint_keys(
        astro_data=astro_data,
        name=user.name,
        birthdate=user.date_of_birth
    )

    return {
        "name": user.name,
        "life_path_number": blueprint.get("Life Path Number"),
        "destiny_number": blueprint.get("Destiny Number"),
        "summary": blueprint.get("Soul Summary"),
        "unlocked_modules": blueprint.get("Unlocked Modules")
    }

@app.get("/")
def read_root():
    return {"message": "Soul Blueprint API is running at https://soulaligned.onrender.com"}