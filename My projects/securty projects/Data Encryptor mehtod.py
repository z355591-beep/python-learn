def encrypt_data(data):
    level = int(input("Enter the level of encryption: "))
    data = data * level
    return data

test = encrypt_data(input("Enter the data to encrypt: "))
print(test)