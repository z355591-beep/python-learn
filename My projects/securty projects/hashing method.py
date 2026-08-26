def hashed(text):
    import hashlib
    return hashlib.sha256(text.encode()).hexdigest()


print(hashed(input("Enter text to hash: ")))