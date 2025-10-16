from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/users", tags=["users"])

users = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"},
}

@router.get("/")
def get_users():
    return list(users.values())

@router.get("/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@router.post("/")
def create_user(user: dict):
    new_id = max(users.keys()) + 1
    user["id"] = new_id
    users[new_id] = user
    return user

@router.put("/{user_id}")
def update_user(user_id: int, updated_user: dict):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id].update(updated_user)
    return users[user_id]

@router.delete("/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted"}