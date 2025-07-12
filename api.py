from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from main import get_all_users, register_user, authenticate_user
from fastapi.middleware.cors import CORSMiddleware
from models.auth import AuthRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/all_users")
async def all_users():
    return {"message": get_all_users()}


@app.post("/register")
async def register(auth: AuthRequest):
    upper_bound = 50
    lower_bound = 5

    username = auth.username
    password = auth.password
    
    if not lower_bound <= len(username) <= upper_bound and lower_bound <= len(password) <= upper_bound:
         raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, 
            detail = "username and password must be between 5 and 50 characters")
    
    message = register_user(username, password)

    if message == "User registered successfully":
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": message})
    elif message == "User already exists":
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=message)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message)
        
   
    
@app.post("/login")
async def login(auth: AuthRequest):
    upper_bound = 50
    lower_bound = 5

    username = auth.username
    password = auth.password

    if not lower_bound <= len(username) <= upper_bound and lower_bound <= len(password) <= upper_bound:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, 
                            detail = "username and password must be between 5 and 50 characters")
    if authenticate_user(username, password):
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content={"message": "login successful"})
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid username or password"
        )