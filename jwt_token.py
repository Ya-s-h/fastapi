# Author: Yash Aggarwal



# Import modules
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException
import status
import os
from dotenv import load_dotenv

# Import local Files
import schema


# Loading .env file
load_dotenv()

# Storing values of environment in local variables
SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = os.environ['ALGORITHM']
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ['ACCESS_TOKEN_EXPIRE_MINUTES'])



def create_token(data: dict):
    """
    Generate access token using SECRET_KEY and ALGORITHM which will expire after ACCESS_TOKEN_EXPIRE_MINUTES
    """

# Encoding data and setting expiry time of token
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
	
# Enconding token using jwt
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str):
	
	"""
	Verify the token user is holding
	"""
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		# Getting the user
		username: str = payload.get("user")
		# If no user is found -> Invalid token
		if username is None:
			# Generating Exception
			credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not a valid user. Are you? huh.\nOr maybe you are away for too long.", 
            headers={"WWW-Authenticate": "Bearer"},
	    )
			raise credentials_exception
		
		token_data = schema.TokenData(username=username)
	except JWTError:
	    raise credentials_exception

# Testing	
if __name__ == "__main__":
    print(create_token(data={"user": "Hello"}))
