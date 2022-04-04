import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

start_time = time.time()


key = os.urandom(32)
iv = os.urandom(16)

with open("context.txt", "rb") as file:
    # read all file data
    file_data = file.read()

message = b"a secret message"


cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

# Encryption
for i in range(100000):
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()
    
execute_time = (time.time() - start_time)
print("--- %s seconds ---" % execute_time)
print("--- {:.2f}bytes/s ---".format(800000/execute_time))

# Decryption
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

print ("-- ECB --")
print ("Ciphertext is:", ciphertext)
print ("Plaintext is:", plaintext)

