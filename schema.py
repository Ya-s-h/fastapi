# Author: Yash Aggarwal



from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Model for signin and signup function
class User(BaseModel):
    username: EmailStr = Field(...)
    password: str = Field(...)

# Model for jwt-token
class TokenData(BaseModel):
    username: Optional[str] = None

