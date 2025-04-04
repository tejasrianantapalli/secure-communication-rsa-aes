from Crypto.PublicKey import RSA

def generate_rsa_keys():
    try:
        key = RSA.generate(2048)

        # Save Private Key
        with open("private.pem", "wb") as priv_file:
            priv_file.write(key.export_key())

        # Save Public Key
        with open("public.pem", "wb") as pub_file:
            pub_file.write(key.publickey().export_key())

        print("✅ RSA Keys Generated Successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    generate_rsa_keys()
