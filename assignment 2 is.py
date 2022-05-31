import ast
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
key = RSA.generate(4096)
f = open('my_rsa_public.pem', 'wb')
f.write(key.publickey().exportKey('PEM'))
f.close()
f = open('my_rsa_private.pem', 'wb')
f.write(key.exportKey('PEM'))
f.close()
f = open('my_rsa_public.pem', 'rb')
key = RSA.importKey(f.read())
message = input("Enter message to Encrypt: ")
encryptor = PKCS1_OAEP.new(key)
encrypted = encryptor.encrypt(bytes(message, 'utf-8'))

print("Encrypted message is", encrypted)
f1 = open('my_rsa_private.pem', 'rb')
key1 = RSA.importKey(f1.read())
message = input("Enter message to Decrypt: ")
decryptor = PKCS1_OAEP.new(key1)
decrypted = decryptor.decrypt(ast.literal_eval(str(message)))
print(decrypted)
