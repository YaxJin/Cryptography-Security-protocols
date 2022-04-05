import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

start_time = time.time()

nonce = os.urandom(16)
key = os.urandom(32)


print ("-- ChaCha20 --")

with open("context.txt", "rb") as file:
    file_data = file.read()

cipher = Cipher(algorithms.ChaCha20(key, nonce),mode=None)

# Encryption
encryptor = cipher.encryptor()
ciphertext = encryptor.update(file_data) + encryptor.finalize()
    
execute_time = (time.time() - start_time)
print("--- %s seconds ---" % execute_time)
print("--- {:.2f}bytes/s ---".format(324867676/execute_time))

# Decryption
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

#print ("Ciphertext is:", ciphertext)
#print ("Plaintext is:", plaintext)

