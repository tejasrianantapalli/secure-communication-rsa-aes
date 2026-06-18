# 🔐 Secure Communication Using RSA and AES

This project demonstrates secure communication using a hybrid cryptographic system combining RSA (asymmetric) and AES (symmetric) encryption. It ensures fast, secure, and efficient encryption and decryption of messages in a networked environment.

---

## 📌 Features

- AES for fast message encryption  
- RSA for secure key exchange  
- Hybrid encryption model (used in HTTPS, messaging apps, etc.)  
- Python-based implementation  
- Easy-to-follow modular code  

---

## 🚀 How to Run

### 1. Generate RSA Key Pair

Run the following command:

```bash

This will generate:

private.pem

public.pem


python generate_keys.py

2. Encrypt the Message
Run the encryption script:

bash
Copy
Edit
python encryption.py
This will:

Generate a random AES key

Encrypt the message using AES

Encrypt the AES key using RSA

Save the encrypted AES key and message into encrypted_data.txt

3. Decrypt the Message
Run the decryption script:

bash
Copy
Edit
python decryption.py
This will:

Read the encrypted AES key and message from encrypted_data.txt

Decrypt the AES key using the RSA private key

Decrypt the original message using the AES key

🛠 Requirements
Install the required package using pip:

bash
Copy
Edit
pip install pycryptodome
📁 Project Structure
pgsql
Copy
Edit
securecommunication/
├── generate_keys.py         # Generates RSA public and private keys
├── encryption.py            # Encrypts message and AES key
├── decryption.py            # Decrypts AES key and message
├── utils.py                 # Contains encryption/decryption helper functions
├── encrypted_data.txt       # Stores encrypted AES key and encrypted message
├── public.pem               # RSA Public Key
├── private.pem              # RSA Private Key
✨ Output Example
pgsql
Copy
Edit
🔐 Encrypted Message: <cipher text>
🔑 Encrypted AES Key: <encrypted key>
🔓 AES Key Decrypted Successfully: True
📩 Decrypted Message: Hello, this is a secure message.
🧠 Concepts Used
AES (Advanced Encryption Standard)

RSA (Rivest–Shamir–Adleman)

Base64 encoding

Public-Key Infrastructure

📜 License
This project is open-source and available under the MIT License.



