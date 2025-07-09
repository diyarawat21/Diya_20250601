from sqlalchemy import Column, Integer, String, ForeignKey , Boolean
from sqlalchemy.orm import relationship
from database import Base

class MapNode(Base):
    __tablename__ = "map_nodes"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    level = Column(String, nullable=True)
    type = Column(String, nullable=True)  # e.g., concept, project, example
    dependency = Column(String, nullable=True)  # e.g., topic id(s)
    is_completed = Column(Boolean, default=False)
    your_note = Column(String, nullable=True)

    workspace_id = Column(Integer, ForeignKey("workspace.id"))
    workspace = relationship("Workspace", back_populates="map_nodes")
