from fastapi import APIRouter
import json

router = APIRouter(prefix="/api/horse_race", tags=["horse_race"])

PROGRESS_FILE_PATH = "/home/devin/projects/cat/saved-data/progress.json"

@router.get("/")
def get_horse_progress():
    try:
        with open(PROGRESS_FILE_PATH, "r") as file:
            data = json.load(file)
    except:
        return {'active': False, 'year': 2000, 'month': 1, 'day': 1}
    
    return data
