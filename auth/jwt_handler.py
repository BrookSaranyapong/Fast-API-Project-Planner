import time
from datetime import datetime

from fastapi import HTTPException, status
from jose import jwt, JWTError
from database.connection import Settings 

setting = Settings()

def create_access_token(user:str):
    payload = {
        "user": user,
        "expires": time.time() + 3600
    }
    token = jwt.encode(payload,setting.SECRET_KEY, algorithm=setting.ALGORITHM)
    return token

def verify_access_token(token:str):
    try:
        data = jwt.decode(token,setting.SECRET_KEY,algorithms=setting.ALGORITHM)
        expire = data.get("expires")
        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied"
            )

        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token Expired!"
            )
        return data
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token"
        )