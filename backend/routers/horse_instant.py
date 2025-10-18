from fastapi import APIRouter
import json
import os
from dotenv import load_dotenv

# resolve enviornmental variables
load_dotenv("../../.env")
INSTANTIATION_FILE_PATH = os.getenv("INSTANTIATION_FILE_PATH")


router = APIRouter(prefix="/api/horse_instant", tags=["horse_instant"])

@router.get("/")
def get_horse_instantiation():
    try:
        with open(INSTANTIATION_FILE_PATH, "r") as file:
            data = json.load(file)
    except:
        return {"data": []}
    
    return data
