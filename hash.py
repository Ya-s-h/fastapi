# Author: Yash Aggarwal



from passlib.context import CryptContext


# Creating obj of CryptContext with bcrypt as Hash Algorihtm
password_context = CryptContext(schemes=['bcrypt'])

class Hash():
    """
    Class for generating bcrypt of plaintext and matching Hash and Plaintext
    
    """

    def genHash(plaintext):
        # Hashing the plaintext
        return password_context.hash(plaintext)
    
    def check(hash, normal):
        # Verifying the hash password
        return password_context.verify(hash=hash, secret=normal)
