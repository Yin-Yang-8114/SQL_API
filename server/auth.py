import csv
from pathlib import Path
import bcrypt
from fastapi import HTTPException
USERS_FILE = Path(__file__).resolve().parent / "users.csv"

def read_users():
    if not USERS_FILE.exists():
        return []
    with USERS_FILE.open("r", encoding="utf-8", newline="") as file:
        users = list(csv.DictReader(file))
    return users

def register_user(username, password):
    username = username.strip()
    if not username or not password.strip():
        raise HTTPException(
            status_code=400,
            detail="Username and password cannot be empty",)
    password_bytes = password.encode("utf-8")

    if len(password_bytes) > 72:
        raise HTTPException(
            status_code=400,
            detail="Password is too long",)
    users = read_users()
    for user in users:
        if user["username"] == username:
            raise HTTPException(
                status_code=409,
                detail="Username already exists",)

    password_hash = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt(),
    ).decode("utf-8")

    file_is_empty = (
        not USERS_FILE.exists()
        or USERS_FILE.stat().st_size == 0)

    with USERS_FILE.open("a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["username", "password_hash"],)
        if file_is_empty:
            writer.writeheader()
        writer.writerow({
            "username": username,
            "password_hash": password_hash,})
    return {"message": "User registered successfully"}

def check_user(username, password):
    username = username.strip()
    password_bytes = password.encode("utf-8")
    if not username or not password.strip():
        return False
    if len(password_bytes) > 72:
        return False
    users = read_users()
    for user in users:
        if user["username"] == username:
            saved_hash = user["password_hash"].encode("utf-8")
            password_is_correct = bcrypt.checkpw(
                password_bytes,
                saved_hash,)
            return password_is_correct
    return False