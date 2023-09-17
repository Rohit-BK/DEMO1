import hashlib

def hash_data(data):
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    return hashed_data

def encrypt_data(data, encryption_key):
    # Implement encryption algorithm here
    encrypted_data = data + encryption_key
    return encrypted_data

def decrypt_data(encrypted_data, encryption_key):
    # Implement decryption algorithm here
    decrypted_data = encrypted_data.replace(encryption_key, "")
    return decrypted_data

if __name__ == "__main__":
    data = "This is a sample data"
    encryption_key = "secret_key"

    hashed_data = hash_data(data)
    print(f"Hashed Data: {hashed_data}")

    encrypted_data = encrypt_data(data, encryption_key)
    print(f"Encrypted Data: {encrypted_data}")

    decrypted_data = decrypt_data(encrypted_data, encryption_key)
    print(f"Decrypted Data: {decrypted_data}")
