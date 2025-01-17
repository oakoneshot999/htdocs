from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend
import os
key = os.urandom(32)  # AES necesită o cheie de 256 biți (32 de octeți)
iv = os.urandom(16)  # Vector de inițializare

# Funcții de criptare și decriptare
def encrypt_data(key, iv, data):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

def decrypt_data(key, iv, ciphertext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

# Funcții de semnare și verificare
def create_signature(private_key, data):
    return private_key.sign(data, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

def verify_signature(public_key, data, signature):
    try:
        public_key.verify(signature, data, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return True
    except Exception as e:
        print(e)
        return False

# Generarea cheilor RSA
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Crearea semnăturii pentru cuvântul "mama"

mesaj = "mama"
mesaj_bytes = mesaj.encode('utf-8')
semnatura = create_signature(private_key, mesaj_bytes)
with open("D:/xampp/htdocs/python/cheie.txt", "wb") as file:
    file.write(semnatura)

# Verificarea semnăturii
if verify_signature(public_key, mesaj_bytes, semnatura):
    print("Semnătura este validă.")

    # Criptarea documentului
    with open("D:/xampp/htdocs/python/document.txt", "rb",encoding='utf-8') as file:
        document_content = file.read()
    criptat_document = encrypt_data(key, iv, document_content)
    with open("D:/xampp/htdocs/python/codatdocument.txt", "wb") as file:
        file.write(criptat_document)
    
    # Decriptarea documentului criptat doar dacă semnătura este validă
    decriptat_document = decrypt_data(key, iv, criptat_document)
    with open("D:/xampp/htdocs/python/documentdecodat.txt", "wb") as file:
        file.write(decriptat_document)

    print("Documentul a fost criptat și decriptat cu succes.")
else:
    print("Semnătura nu este validă.")
