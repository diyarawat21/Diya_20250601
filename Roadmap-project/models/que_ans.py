from sqlalchemy import Column, Integer, JSON, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class QuestionAnswer(Base):
    __tablename__ = "question_answers"

    id = Column(Integer, primary_key=True)
    ques_ans = Column(JSON, nullable=False)  # storing whole block of Q&A
    workspace_id = Column(Integer, ForeignKey("workspace.id"))

    workspace = relationship("Workspace", back_populates="question_answers")
