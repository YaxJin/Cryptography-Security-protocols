import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

start_time = time.time()


key = os.urandom(32)
iv = os.urandom(16)

print ("-- CTR --")


with open("context.txt", "rb") as file:
    file_data = file.read()

padder = padding.PKCS7(128).padder()
padded_data = padder.update(file_data)
cipher = Cipher(algorithms.AES(key), modes.CTR(iv))

# Encryption
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
execute_time = (time.time() - start_time)
print("--- %s seconds ---" % execute_time)
print("--- {:.2f}bytes/s ---".format(324867676/execute_time))

# Decryption
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()


#print ("Ciphertext is:", ciphertext)
#print ("Plaintext is:", plaintext)
