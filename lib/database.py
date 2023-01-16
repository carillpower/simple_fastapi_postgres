import sqlalchemy as sa
import sqlalchemy.ext.declarative as d
import sqlalchemy.orm as orm

DB_CONN = "postgresql://admin:password@localhost:5432/test_db"
engine = sa.create_engine(DB_CONN)

SessionLocal = orm.sessionmaker(
  autocommit=False, 
  autoflush=False,
  bind=engine
  )

Base = d.declarative_base()

