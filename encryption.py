from utils import encrypt_aes, encrypt_aes_key
from Crypto.Random import get_random_bytes

# Generate AES key
aes_key = get_random_bytes(16)

# Encrypt message
message = "Hello, this is a secure message."
encrypted_message = encrypt_aes(message, aes_key)
print(f"🔐 Encrypted Message: {encrypted_message}")

# Encrypt AES key using RSA
encrypted_aes_key = encrypt_aes_key(aes_key)
print(f"🔑 Encrypted AES Key: {encrypted_aes_key}")

# Save encrypted AES key
with open("encrypted_aes_key.txt", "w") as file:
    file.write(encrypted_aes_key)

# Save encrypted message
with open("encrypted_message.txt", "w") as file:
    file.write(encrypted_message)

print("✅ Encrypted data saved successfu