import uuid
from sqlmodel import Field, SQLModel
from pydantic import EmailStr


class UserBaseWithoutPassword(SQLModel):
    name: str
    last_name: str
    email: EmailStr = Field(unique=True)


class UserBase(UserBaseWithoutPassword):
    password: str


class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class UserCreate(UserBase):
    pass


class UserLogin(SQLModel):
    email: EmailStr = Field(unique=True)
    password: str


class UserPublic(UserBaseWithoutPassword):
    id: uuid.UUID
