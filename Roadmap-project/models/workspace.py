from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base
from database import Base


class Workspace(Base):
    __tablename__ = "workspace"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("user_table.id"), nullable=False)
    progress = Column(Integer, default=0)
    prior_knowledge = Column(String, nullable=True)

    root_node_id = Column(Integer, ForeignKey("map_nodes.id"), nullable=True)

    # Relationships to users
    user = relationship("User", back_populates="workspaces")
    # Relationships to map nodes
    map_nodes = relationship("MapNode", back_populates="workspace", cascade="all, delete-orphan")
    # Relationships to root node 
    root_node = relationship("MapNode", foreign_keys=[root_node_id])

    # ✅ Add this relationship to link workspace to question_answer table
    question_answer = relationship("QuestionAnswer", back_populates="workspace", cascade="all, delete-orphan")
