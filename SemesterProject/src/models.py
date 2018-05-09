from sqlalchemy import (
    Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Listing(Base):
    '''
    Class representing the table of telephone listings.

    '''
    
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    country_code = Column(Integer, nullable=False)
    phone_number = Column(Integer, nullable=False)

    def __init__(self, **kwargs):
        super(Listing, self).__init__(**kwargs)

    def __repr__(self):
        return f'<Listing {self.name}, {self.phone_number}>'

