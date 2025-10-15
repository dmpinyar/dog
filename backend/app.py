from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS to allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory "database"
users = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"},
}

@app.get("/api/users")
def get_users():
    return list(users.values())

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.post("/api/users")
def create_user(user: dict):
    new_id = max(users.keys()) + 1
    user["id"] = new_id
    users[new_id] = user
    return user

@app.put("/api/users/{user_id}")
def update_user(user_id: int, updated_user: dict):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id].update(updated_user)
    return users[user_id]

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "User deleted"}

