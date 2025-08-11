from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime


class UserResponse(BaseModel):
    id: UUID
    # email: EmailStr
    email: str
    first_name: str
    last_name: str


class PasswordChange(BaseModel):
    current_password: str
    new_password: str
    new_password_confirm: str
