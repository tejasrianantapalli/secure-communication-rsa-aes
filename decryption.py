from utils import decrypt_aes_key, decrypt_aes  # Ensure utils.py is correctly referenced
import base64

# Load Encrypted AES Key (Assuming it's stored in a file or passed)
try:
    with open("encrypted_aes_key.txt", "r") as file:
        encrypted_aes_key = file.read().strip()
except FileNotFoundError:
    print("❌ ERROR: Encrypted AES key file not found!")
    exit(1)

print(f"🔑 Encrypted AES Key Loaded: {encrypted_aes_key}")

# Decrypt AES Key
decrypted_aes_key = decrypt_aes_key(encrypted_aes_key)

if decrypted_aes_key:
    print(f"✅ AES Key Decrypted Successfully: {decrypted_aes_key.hex()}")
else:
    print("❌ ERROR: AES Key Decryption Failed!")
    exit(1)

# Load Encrypted Message
try:
    with open("encrypted_message.txt", "r") as file:
        encrypted_message = file.read().strip()
except FileNotFoundError:
    print("❌ ERROR: Encrypted message file not found!")
    exit(1)

print(f"📩 Encrypted Message Loaded: {encrypted_message}")

# Decrypt Message
try:
    decrypted_message = decrypt_aes(encrypted_message, decrypted_aes_key)
    print(f"📩 Decrypted Message: {decrypted_message}")
except ValueError:
    print("❌ ERROR: Message decryption failed! Possible key mismatch.")


