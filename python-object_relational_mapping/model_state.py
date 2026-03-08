#!/usr/bin/python3
"""
contains the class definition of a State
and an instance Base = declarative_base()
"""

# import modules
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create instance of declarative_base
Base = declarative_base()

# create State class definition
class State(Base):
    """State class definition"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)