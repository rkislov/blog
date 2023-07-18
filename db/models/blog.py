from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

from db.base import Base

class Blog(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    author_id =  Column(UUID,ForeignKey("user.id"))
    author = relationship("User",back_populates="blogs")
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)