from sqlalchemy import Column, String, Boolean, Integer
from entity import Entity, Base

class Inventory(Entity, Base):
    __tablename__ = 'inventory'

    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    available = Column(Boolean)
    color = Column(String)

    def __init__(self, make, model, year, available, color):
        Entity.__init__(self)
        self.make = make
        self.model = model
        self.year = year
        self.available = available
        self.color = color
