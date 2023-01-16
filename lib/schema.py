import datetime as dt
import pydantic as py

class BaseUserList(py.BaseModel):
  fname: str
  lname: str
  email: str
  phone: str

class UserList(BaseUserList):
  id: int
  created_at: dt.datetime

  ## ERROR: pydantic.errors.ConfigError: You must have the config attribute orm_mode=True to use from_orm
  class Config:
    orm_mode = True

class CreateUser(BaseUserList):
  pass 


