from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from datetime import datetime


class Project(Base) :
    __tablename__ = 'projects'

    project_id = Column(String, primary_key = True, comment = 'pk')
    project_name = Column(String, nullable = False, unique = True, comment = '프로젝트명')
    description = Column(Text, nullable = True, comment = '설명')
    created_datetime = Column('created_at', DateTime, server_default = current_timestamp())


class Model(Base) :
    __tablename__ = 'models'

    id = Column(Integer, primary_key = True, autoincrement = True)
    modelname = Column('modelname', String)
    projectid = Column(Integer, ForeignKey('project.id'))
    project = relationship('Project', backref = 'models')
    description = Column('description', String, nullable = True)


class Experiment(Base) :
    __tablename__ = 'experiments'

    id = Column(Integer, primary_key = True, autoincrement = True)
    modelid = Column(Integer, ForeignKey('model.id'))
    model = relationship('Model', backref= 'experiments')
    projectid = Column(Integer, ForeignKey('project.id'))
    description = Column('description', String, nullable = True)

