# Author: Yash Aggarwal



from fastapi import Depends
from jwt_token import verify_token
from fastapi.security import OAuth2PasswordBearer

# For Verifying the current logged in user by validating the token from /login url
oauth2scheme = OAuth2PasswordBearer(tokenUrl="login")


#function to find the current user that generated the token
def get_current_user(token:str = Depends(oauth2scheme)):
    """
    Will Check if the current logged in user is valid user from its jwt token
    If yes then all good.
    But if not then send an exception
    """
    
    return verify_token(token)