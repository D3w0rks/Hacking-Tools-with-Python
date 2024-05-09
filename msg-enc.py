from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()

def encrypt(key,msg):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(msg.encode())
    return encrypted

def decrypt(key,encrypted):
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted).decode('utf-8')
    return decrypted

if __name__ == '__main__':
    key = Fernet.generate_key()
    msg = input("Enter message to encrypt: ")

    encrypted_msg = encrypt(key,msg)
    print(f"Encrypted message: {encrypted_msg}")

    decrypted_msg = decrypt(key,encrypted_msg)
    print(f"Decrypted message: {decrypted_msg}")

    print(f"Your encryption key: {key}")


