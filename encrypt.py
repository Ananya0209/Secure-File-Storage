import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from file import window_input, openFile, openFiles

def AESalgo():
    key = AESGCM.generate_key(bit_length=128)
    iv = os.urandom(12)
    aad = b'authenticated but encrypted data'
    return key, iv, aad

# def key_encrypt(plaintext, key, iv, add):
 
def encryptFile(key, iv, aad):
    filepath = openFile()
    f = open(filepath, "r")
    content = f.read()
    f.close()
    content = content.encode('utf-8')
    cipher = AESGCM(key)
    ciphertext = cipher.encrypt(iv,content,aad)
    print(content, ciphertext)
    
    
<<<<<<< HEAD
def AESGCM_encrypt(plaintext):
    aad = b'authenticated but encrypted data'
    iv = os.urandom(12) #96-bit initialization vector
    key = AESGCM.generate_key(bit_length=128)    #128-bit key
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(iv, plaintext, aad)

    return ciphertext, iv, key

def decrypt(ciphertext,key,iv):
    aad = b'authenticated but encrypted data'
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(iv, ciphertext, aad) 
    return plaintext
=======
>>>>>>> 63bbabdd635f0f96e1185e73e31f81f0312846bb

def main():
    key, iv , aad = AESalgo() 
    encryptFile(key, iv, aad)
main()
    


    
