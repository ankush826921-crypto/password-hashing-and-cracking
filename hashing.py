import os
import hashlib
import json
from typing import Dict, Any

USERS_DB_FILE = "users.json"


def generate_salt(length: int = 16) -> str:
    """
    Random salt generate karta hai (hex string).
    """
    return os.urandom(length).hex()


def hash_password(password: str, salt: str) -> str:
    """
    Password + salt ko SHA-256 se hash karta hai.
    Return: hex digest.
    """
    combo = (salt + password).encode("utf-8")
    return hashlib.sha256(combo).hexdigest()


def load_users_db() -> Dict[str, Any]:
    """
    users.json file se data load karta hai.
    Agar file nahi ho to empty dict return karega.
    """
    if not os.path.isfile(USERS_DB_FILE):
        return {}
    with open(USERS_DB_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_users_db(data: Dict[str, Any]) -> None:
    """
    users.json me data save karta hai.
    """
    with open(USERS_DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def register_user(username: str, password: str) -> None:
    """
    Naya user create karta hai:
    - Random salt
    - Salted SHA-256 hash
    - users.json me store
    """
    users = load_users_db()
    if username in users:
        raise ValueError("Username already exists.")

    salt = generate_salt()
    password_hash = hash_password(password, salt)

    users[username] = {
        "salt": salt,
        "password_hash": password_hash,
    }
    save_users_db(users)


def verify_login(username: str, password: str) -> bool:
    """
    Username + password ko verify karta hai users.json se.
    """
    users = load_users_db()
    if username not in users:
        return False

    salt = users[username]["salt"]
    expected_hash = users[username]["password_hash"]
    given_hash = hash_password(password, salt)
    return given_hash == expected_hash
