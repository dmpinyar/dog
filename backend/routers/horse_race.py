from fastapi import APIRouter
import json

router = APIRouter(prefix="/api/horse_race", tags=["horse_race"])

PROGRESS_FILE_PATH = "/home/devin/projects/cat/saved-data/progress.json"
MAX_LENGTH = 20

horse_data = []

@router.get("/")
def get_horse_progress():
    global horse_data

    try:
        with open(PROGRESS_FILE_PATH, "r") as file:
            individual = json.load(file)
    except:
        return horse_data
    
    if (individual["active"] and (individual["horses"] > 0) and (not horse_data or individual["day"] != horse_data[0]["day"])):
        horse_data = [individual] + horse_data
        horse_data = horse_data[:MAX_LENGTH]

    return horse_data

# @router.post("/")
# def save_progress(horse: dict):
#     global horse_data
#     horse_data = [horse] + horse_data
#     horse_data = horse_data[:MAX_LENGTH]
#     return horse_data[0]