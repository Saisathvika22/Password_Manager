from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Save this key safely:")
print(key)