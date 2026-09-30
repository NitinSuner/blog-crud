from sqlmodel import SQLModel , Field
from typing import Optional

class Blog(SQLModel, table=True): #SQLmodel = kya banana hai tumhe, table=true => table main entry honi chahiye ya nahi
    id : Optional[int] = Field(default=None, primary_key=True)
    title : str
    description :str
    ispublished:str