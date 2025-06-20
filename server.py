import os
import sqlite3
from typing import List
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# Initialize FastAPI application
app = FastAPI()

# Mount the static directory to serve assets
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Set up templates folder
templates = Jinja2Templates(directory="./")

# Get the env type: (this must be set by Dockerfile)
env_type = os.getenv("ENV_TYPE", "⚠️ ERROR !!")


# Return base HTML page
@app.get("/")
def index(request: Request):
    users = get_users()
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
            "users": users,
            "env_type": env_type
        }
    )


# Helper Function:
def get_users() -> List[dict[str, dict[str, str]]]:
    with sqlite3.connect(database="./users.db") as conn:
        cursor = conn.cursor()
        command = "SELECT * FROM USERS;"
        cursor.execute(command)
        entries = cursor.fetchall()

        users = []
        for entry in entries:
            users.append({
                "id": entry[0],
                "first_name": entry[1],
                "last_name": entry[2],
                "email": entry[3],
                "dob": entry[4],
            })
        return users


if __name__ == "__main__":
    import uvicorn
    os.makedirs("assets", exist_ok=True)
    uvicorn.run(app, host="0.0.0.0", port=7575)
