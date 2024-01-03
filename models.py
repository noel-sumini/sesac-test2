from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationships
from database import Base

class Post(Base):
    __tablename__ = "post"

    post_id = Column(Integer, primary_key = True, autoincrement= True)
    title = Column(Text, nullable = False)
    content = Column(Text, nullable = True)
    writer = Column(Text, nullable = False)