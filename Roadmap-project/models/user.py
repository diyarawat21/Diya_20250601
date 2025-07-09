from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models import user, workspace, map_nodes, que_ans


class User(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    workspaces = relationship("Workspace", back_populates="user", cascade="all, delete")
