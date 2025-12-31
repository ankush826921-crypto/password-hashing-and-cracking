# Password Hashing & Cracking (Python) 🔐

Cybersecurity Internship Project – **Password Cracking and Hashing Algorithms**

## 🎯 Objective

Demonstrate how:
- Passwords should be stored securely using **salted hashing**
- Weak passwords can be cracked using a simple **dictionary attack**

This project is for learning and ethical use only.

---

## ✨ Features

- **User Registration**
  - Generates a random salt per user
  - Stores `salt + SHA-256(password)` in `users.json`
- **User Login**
  - Verifies password by recomputing salted hash
- **View Stored Hashes**
  - Shows username, salt, and password hash (for demo)
- **SHA-256 Hash Demo**
  - Hash any input string with SHA-256
- **Dictionary-based Hash Cracker**
  - Takes a SHA-256 hash and tries to recover the password using a wordlist

---

## 🛠️ Tech Stack

- Python 3.x
- Standard Library:
  - `hashlib` (SHA-256 hashing)
  - `os` (random salt)
  - `json` (simple storage)

No external dependencies required.

---

## 📁 Project Structure

```text
password-hashing-and-cracking/
├── main.py          # CLI menu (register, login, hash demo, cracking)
├── hashing.py       # Salted hashing + user DB logic
├── cracker.py       # Dictionary-based SHA-256 hash cracker
├── wordlist.txt     # Sample password wordlist
└── users.json       # Auto-created: stores users and password hashes

---

## 🎓 Skills Demonstrated
- Secure password storage using salted SHA-256 hashing
- Understanding of hashing vs plaintext passwords
- Basic authentication flow (register + login)
- Dictionary-based password cracking (wordlist attack)
- File-based JSON “database” handling
- CLI-based tooling and input validation

---

## Output

<img width="572" height="1021" alt="Image" src="https://github.com/user-attachments/assets/1b57a010-e180-4321-8a54-c2bd7cc3d6ee" />

---

**Submitted for CodeTech Technologies Internship**  
**Project 7: Password Cracking and Hashing Algorithms**
