import lib.database as db
import lib.models as models
import lib.schema as schema

# def _create_db():
#   return database.Base.metadata.create_all(bind=database.engine)

def _add_tables():   ## Will automatically load class in models.py
  return db.Base.metadata.create_all(bind=db.engine)

def get_db(): ## Make connection
  conn = db.SessionLocal()
  try:
    yield conn
  finally:
    conn.close()

async def create_user(user: schema.CreateUser, db:"Session") -> schema.UserList:
  user = models.UserList(**user.dict())
  db.add(user)
  db.commit()
  db.refresh(user)
  return schema.UserList.from_orm(user)

async def get_all_user(db: "Session") -> list[schema.UserList]:
  user = db.query(models.UserList).all()
  return list(map(schema.UserList.from_orm, user))

async def get_user(id: int, db: "Session"):
  user = db.query(models.UserList).filter(models.UserList.id == id).first()
  return user

async def del_user(user: models.UserList, db: "Session"):
  db.delete(user)
  db.commit()

async def update_user(
  user_data: schema.CreateUser, ## Existing function tht should follow
  user: models.UserList, ## Existing table to be updated
  db: "Session") -> schema.UserList:
  user.fname = user_data.fname
  user.lname = user_data.lname
  user.email = user_data.email
  user.phone = user_data.phone

  db.commit()
  db.refresh(user)
  return schema.UserList.from_orm(user)














