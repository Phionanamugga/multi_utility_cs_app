
#from .hashers import hash_password


def hash_password(password: str) -> str:
    # Example hashing implementation using SHA256
    import hashlib
    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed


