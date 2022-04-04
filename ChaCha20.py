import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms

start_time = time.time()

nonce = os.urandom(16)
key = os.urandom(32)


message = b"a secret message"


cipher = Cipher(algorithms.ChaCha20(key, nonce),mode=None)

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

print ("-- ChaCha20 --")
print ("Ciphertext is:", ciphertext)
print ("Plaintext is:", plaintext)

