from fastapi import APIRouter
import json

router = APIRouter(prefix="/api/horse_instant", tags=["horse_instant"])

INSTANTIATION_FILE_PATH = "/home/devin/projects/cat/saved-data/instantiation.json"

@router.get("/")
def get_horse_instantiation():
    try:
        with open(INSTANTIATION_FILE_PATH, "r") as file:
            data = json.load(file)
    except:
        return json.load({"startYear": 2000, 
                "startMonth": 1,
                "startDay": 1,
                "endYear": 2000, 
                "endMonth": 1,
                "endDay": 1})
    
    return data


    

