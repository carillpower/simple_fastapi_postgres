from typing import TYPE_CHECKING, List
import fastapi as fa
import sqlalchemy.orm as orm
import lib.schema as schema
import svc

if TYPE_CHECKING:
  from sqlalchemy.orm import Session

app = fa.FastAPI()

## Insert
@app.post('/api/userlist/', response_model=schema.UserList)
async def create_user(
  user: schema.CreateUser, db: orm.Session = fa.Depends(svc.get_db)
):
  return await svc.create_user(user=user, db=db)


## Select
@app.get('/api/userlist/', response_model=List[schema.UserList])
async def get_all_user(db: orm.Session = fa.Depends(svc.get_db)):
  return await svc.get_all_user(db=db)


## Select where
@app.get('/api/userlist/{id}', response_model=schema.UserList)
async def get_user(id: int, db: orm.Session = fa.Depends(svc.get_db)):
  user = await svc.get_user(db=db, id=id)
  if user is None:
    raise fa.HTTPException(status_code=404, detail="User not exists")

  # return await svc.get_user(id=id, db=db)
  return user


## Delete where
@app.delete('/api/userlist/{id}')
async def del_user(id: int, db: orm.Session = fa.Depends(svc.get_db)):
  user = await svc.get_user(db=db, id=id)
  if user is None:
    raise fa.HTTPException(status_code=404, detail="User not exists")

  await svc.del_user(user, db=db)
  return f"User ID {id} successfully deleted"


## Update where
@app.put('/api/userlist/{id}', response_model=schema.UserList)
async def update_user(id: int, user_data: schema.CreateUser, db: orm.Session = fa.Depends(svc.get_db)):
  user = await svc.get_user(db=db, id=id)
  if user is None:
    raise fa.HTTPException(status_code=404, detail="User not exists")
  
  return await svc.update_user(user_data=user_data, user=user, db=db)



