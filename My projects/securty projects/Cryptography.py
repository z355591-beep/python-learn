from cryptography.fernet import Fernet

text = input("Enter your message to encrypt: ")

def encrypt_message(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

key = Fernet.generate_key()

encrypted = encrypt_message(text, key)
decrypted = decrypt_message(encrypted, key)

print(f"Original message: {text}")
print(f"Encrypted message: {encrypted}")
print(f"Decrypted message: {decrypted}")