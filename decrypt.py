import os
from cryptography.fernet import Fernet

for file in os.listdir():
    if file == "crypto.py" or file == ".git" or file == "key.key" or file == "decrypt.py":
        continue
    else:
        with open("key.key",'rb') as theKey:
            key = theKey.read()

        with open(file,"rb") as fl:
            data = fl.read()

        with open(file,"wb") as fl:
            data = Fernet(key).decrypt(data)
            fl.write(data)

print("Done")