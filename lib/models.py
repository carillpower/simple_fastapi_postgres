import datetime as dt
import sqlalchemy as sa
import lib.database as db

## Create Table userlist
class UserList(db.Base):
  __tablename__ = 'userlist'
  id = sa.Column(sa.Integer, primary_key=True, index=True)
  fname = sa.Column(sa.String, index=False)
  lname = sa.Column(sa.String, index=False)
  email = sa.Column(sa.String, index=False)
  phone = sa.Column(sa.String, index=False, unique=True)
  created_at = sa.Column(sa.DateTime, default=dt.datetime.utcnow)

