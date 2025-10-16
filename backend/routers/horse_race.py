from fastapi import APIRouter
import json

router = APIRouter(prefix="/api/horse_race", tags=["horse_race"])

PROGRESS_FILE_PATH = "/home/devin/projects/cat/saved-data/progress.json"
MAX_LENGTH = 20
# HORSE_DATA_PATH = "/home/devin/projects/dog/backend/stored-data/horse_data.np"

@router.get("/")
def get_horse_progress():
    try:
        with open(PROGRESS_FILE_PATH, "r") as file:
            horse_data = json.load(file)
        #horse_data = numpy.load(HORSE_DATA_PATH)
    except:
        #horse_data = numpy.array([])
        horse_data = {"data":[]}

    # if (current["active"] and (current["horses"] > 0) and (not horse_data or current["day"] != horse_data[0]["day"])):
    #     horse_data = numpy.insert(horse_data, 0, current)
    #     horse_data = horse_data[:MAX_LENGTH]
    
    # numpy.save(HORSE_DATA_PATH, horse_data)

    return horse_data["data"]

# @router.post("/")
# def save_progress(horse: dict):
#     global horse_data
#     horse_data = [horse] + horse_data
#     horse_data = horse_data[:MAX_LENGTH]
#     return horse_data[0]