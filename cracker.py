import hashlib
from typing import Optional


def sha256_hash(text: str) -> str:
    """
    Simple SHA-256 hash helper.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def crack_sha256_hash(target_hash: str, wordlist_path: str) -> Optional[str]:
    """
    Simple dictionary-based password cracker.

    - wordlist file se passwords read karta hai
    - har line ka SHA-256 hash banata hai
    - target_hash se compare karta hai
    - match milne par original password return karta hai
    """
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                candidate = line.strip()
                if not candidate:
                    continue
                candidate_hash = sha256_hash(candidate)
                if candidate_hash == target_hash:
                    return candidate
    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist_path}")
    return None
