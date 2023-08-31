from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Project(Base) :
    __tablename__ = 'project'

    id = Column('id', Integer, primary_key = True, autoincrement = True)
    projectname = Column('projectname', String)
    description = Column('description', String, nullable = True)
    created_at = Column('created_at', DateTime, default = datetime.now())


class Model(Base) :
    __tablename__ = 'model'

    id = Column(Integer, primary_key = True, autoincrement = True)
    modelname = Column('modelname', String)
    projectid = Column(Integer, ForeignKey('project.id'))
    project = relationship('Project', backref = 'models')
    description = Column('description', String, nullable = True)


class Experiment(Base) :
    __tablename__ = 'experiment'

    id = Column(Integer, primary_key = True, autoincrement = True)
    modelid = Column(Integer, ForeignKey('model.id'))
    model = relationship('Model', backref= 'experiments')
    projectid = Column(Integer, ForeignKey('project.id'))
    description = Column('description', String, nullable = True)

