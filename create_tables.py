from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Base, Student

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

def commit():
    student = Student("1BG22CS008", "Check", "22cse032@bnmit.in")
    session.add(student)
    session.commit()  # Commit the changes to the database
