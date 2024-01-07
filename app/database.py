from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:xJOYce$%^@localhost/fastapi"
#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#     # Connect to an existing database
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                              password='xJOYce$%^', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error:", error)
#         time.sleep(2)
