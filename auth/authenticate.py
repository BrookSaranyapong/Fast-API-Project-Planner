from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from auth.jwt_handler import verify_access_token

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/user/signin")

async def authenticate(token:str = Depends(oauth2_schema)):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not token provide!"
        )

    decoded_token = verify_access_token(token)
    print("********")   
    print(token)
    print("********")   

    return decoded_token["user"]
