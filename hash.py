# Author: Yash Aggarwal



from passlib.context import CryptContext


password_context = CryptContext(schemes=['bcrypt'])

class Hash():

    def genHash(plaintext):
        return password_context.hash(plaintext)
    
    def check(hash, normal):
        return password_context.verify(hash=hash, secret=normal)