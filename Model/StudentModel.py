from pydantic import BaseModel, Field,EmailStr
from typing import Annotated


class StudentStruct(BaseModel):
    roll:Annotated[int, Field(title="Enter your roll ")]
    name:Annotated[str, Field(title="Enter your name ")]
    age:Annotated[int, Field(title="Enter your age ")]
    email:Annotated[EmailStr, Field(title="Enter your email ")]
