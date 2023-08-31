from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, relationship
from datetime import datetime


class Project(Base) :
    __tablename__ = 'experiment'

    id = Column('id', Integer, primary_key = True, autoincrement = True)
    projectname = Column('projectname', String)
    description = Column('description', String, nullable = True)
    created_at = Column('created_at', DateTime, default = datetime.now())


class Model(Base) :
    __tablename__ = 'model'

    id = Column(Integer, primary_key = True, autoincrement = True)
    modelname = Column('modelname', String)
    projectid = Column(Integer, ForeignKey('project.id'))
    project = relationship('Project', backref = 'project')
    description = Column('description', String)


class Experiment(Base) :
    __tablename__ = 'experiment'

    id = Column(Integer, primary_key = True, autoincrement = True)
    modelid = Column(Integer, ForeignKey('model.id'))
    projectid = Column(Integer, ForeignKey('project.id'))
    description = Column('description', String)

