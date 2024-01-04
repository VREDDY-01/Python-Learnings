s = input("Enter your password")
key = input("Enter a key")

def decrypt(s,key):
     return s.replace(key,"")
    
    
def encrypt(s,key):
    encryptedPass = ""
    for ch in s:
        ch+=key
        encryptedPass+=ch
    return encryptedPass

enPass = encrypt(s,key)
print(enPass)
depass = decrypt(enPass,key)
print(depass)