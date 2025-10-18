from fastapi import APIRouter
import json
import os
from dotenv import load_dotenv

# resolve enviornmental variables
load_dotenv("../../.env")
PROGRESS_FILE_PATH = os.getenv("PROGRESS_FILE_PATH")

router = APIRouter(prefix="/api/horse_race", tags=["horse_race"])

@router.get("/")
def get_horse_progress():
    try:
        with open(PROGRESS_FILE_PATH, "r") as file:
            horse_data = json.load(file)
    except:
        horse_data = {"data":[]}

    return horse_data["data"]