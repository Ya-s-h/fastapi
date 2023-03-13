# Author: Yash Aggarwal



# Loading modules
from fastapi import FastAPI, HTTPException, Depends, Request,status
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException, Depends, Request,status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Loading local files
from schema import User
from jwt_token import create_token
from hash import Hash
from oauth import get_current_user




# Loading .env and storing required env variables in local variables
load_dotenv()
MONGO_URL = os.environ["MONGO_URL"]
PORT = int(os.environ["PORT"] )



# Initialising app
app = FastAPI()
origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialising database
mongoClient = MongoClient(MONGO_URL, PORT)
database = mongoClient['User_Details']


# Creating API for home page ‾\_('‿')_/‾
@app.get('/')
def home_page(current_user: User= Depends(get_current_user)):
    return {
        "message" : "Welcome to Home Page",
        "status code" : 200
    }


@app.post('/signup')
def create_user(data: User):
    HPass = Hash.genHash(plaintext=data.password)
    Username = data.username
    dbObj = {
        "user": Username,
        "password": HPass
    }
    database['users'].insert_one(dbObj)
    
    return {
        "User": Username,
        "Status": 200,
        "message": "User Created Successfully!"
    }


@app.post('/signin')
def signin(data: OAuth2PasswordRequestForm = Depends(User)):
    Username = data.username
    user = database["users"].find_one({
        "user": Username
    })

    if not user or not Hash.check(user['password'], data.password ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong pair of Username and Password is inserted", 
            headers={"WWW-Authenticate": "Bearer"},
	    )
    access_token = create_token(data={"user": user["user"] })
    return {"access_token": access_token, "token_type": "bearer"}


