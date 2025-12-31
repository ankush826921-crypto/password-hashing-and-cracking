from hashing import register_user, verify_login, load_users_db
from cracker import crack_sha256_hash
import hashlib

BANNER = """
=============================================
   PASSWORD HASHING & CRACKING DEMO (Python)
=============================================
"""


def print_users_summary():
    users = load_users_db()
    if not users:
        print("No users registered yet.\n")
        return

    print("Registered users and their hashes:")
    for username, info in users.items():
        print(f"- {username}:")
        print(f"    salt         = {info['salt']}")
        print(f"    password_hash= {info['password_hash']}")
    print()


def register_flow():
    print("\n[REGISTER NEW USER]")
    username = input("Enter new username: ").strip()
    password = input("Enter password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty.\n")
        return

    try:
        register_user(username, password)
        print(f"User '{username}' registered successfully!\n")
    except ValueError as e:
        print(f"Error: {e}\n")


def login_flow():
    print("\n[LOGIN]")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if verify_login(username, password):
        print("Login successful! ✅\n")
    else:
        print("Login failed! ❌\n")


def crack_hash_flow():
    print("\n[HASH CRACKING DEMO]")
    target = input("Enter SHA-256 hash to crack: ").strip()
    wordlist_path = input("Enter wordlist path [wordlist.txt]: ").strip()
    if not wordlist_path:
        wordlist_path = "wordlist.txt"

    print("\n[*] Starting dictionary attack...")
    password = crack_sha256_hash(target, wordlist_path)
    if password:
        print(f"[+] Password found: {password}\n")
    else:
        print("[-] Password not found in wordlist.\n")


def simple_hash_demo_flow():
    print("\n[SIMPLE SHA-256 HASH DEMO]")
    text = input("Enter text to hash: ").strip()
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(f"SHA-256('{text}') = {digest}\n")


def main_menu():
    print(BANNER)
    while True:
        print("Select an option:")
        print("1) Register user (hash + salt password)")
        print("2) Login (verify hashed password)")
        print("3) Show users (salt + hashes)")
        print("4) Simple SHA-256 hash demo")
        print("5) Crack SHA-256 hash (dictionary attack)")
        print("6) Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            register_flow()
        elif choice == "2":
            login_flow()
        elif choice == "3":
            print_users_summary()
        elif choice == "4":
            simple_hash_demo_flow()
        elif choice == "5":
            crack_hash_flow()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1–6.\n")


if __name__ == "__main__":
    main_menu()
