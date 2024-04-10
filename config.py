from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'Student'

    usn = Column(String, primary_key=True)  # Assuming usn is the primary key
    name = Column(String)
    email = Column(String)

    def __init__(self, usn, name, email):
        self.usn = usn
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Student(usn={self.usn}, name={self.name}, email={self.email})"
