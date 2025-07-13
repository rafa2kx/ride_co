from datetime import date
from sqlalchemy import Column, DateTime, Integer, String
from extension import db

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=db.func.current_timestamp())
    created_by = Column(String, nullable=False, default='system')
    updated_at = Column(DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    updated_by = Column(String, nullable=False, default='system')
    
    def as_dict(self):
       dict = {}
       for c in self.__table__.columns:
           value = getattr(self, c.name)
           if isinstance(value, date ):# or isinstance(value, Decimal):
               value = str(value)
           dict[c.name] = None if value is None else value
       return dict

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"
