from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

# AES Encryption
def encrypt_aes(plain_text, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode())
    return base64.b64encode(nonce + ciphertext).decode()

# AES Decryption
def decrypt_aes(cipher_text, key):
    data = base64.b64decode(cipher_text)
    nonce = data[:16]
    ciphertext = data[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()

# Encrypt AES Key with RSA
def encrypt_aes_key(aes_key, public_key_file="public.pem"):
    with open(public_key_file, "rb") as file:
        public_key = RSA.import_key(file.read())
    
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_key = cipher_rsa.encrypt(aes_key)
    
    return base64.b64encode(encrypted_key).decode()

# Decrypt AES Key with RSA
def decrypt_aes_key(encrypted_aes_key, private_key_file="private.pem"):
    with open(private_key_file, "rb") as file:
        private_key = RSA.import_key(file.read())
    
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_key = cipher_rsa.decrypt(base64.b64decode(encrypted_aes_key))
    
    return decrypted_key
