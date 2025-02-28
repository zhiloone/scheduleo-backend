from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError
import bcrypt


from app.db import get_session

from .models import User, UserCreate, UserPublic


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/signup/", response_model=UserPublic)
async def sign_up(*, db: Session = Depends(get_session), user: UserCreate):
    db_user = User.model_validate(user)
    print(db_user)
    hashed_password = bcrypt.hashpw(db_user.password.encode("utf8"), bcrypt.gensalt())
    db_user.password = hashed_password
    db.add(db_user)

    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")

    user_dict = db_user.model_dump()
    user_dict.pop("password")
    return user_dict
