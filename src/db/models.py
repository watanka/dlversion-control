from src.db.database import Base
from sqlalchemy import Column, JSON, String, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from datetime import datetime


class Project(Base) :
    __tablename__ = 'projects'

    project_id = Column(String, primary_key = True, comment = 'pk')
    project_name = Column(String, nullable = False, unique = True, comment = '프로젝트명')
    description = Column(Text, nullable = True, comment = '설명')
    created_datetime = Column(DateTime(timezone = True), server_default = current_timestamp(), nullable = False)


class Model(Base) :
    __tablename__ = 'models'

    model_id = Column(String(255), primary_key = True, comment = 'pk')
    project_id = Column(String(255), ForeignKey('projects.project_id'), nullable = False, comment = 'fk')
    model_name = Column(String(255), nullable = False, comment = '모델명')
    description = Column(Text, nullable = True, comment = '설명')
    created_datetime = Column(DateTime(timezone = True), server_default = current_timestamp(), nullable = False)


class Experiment(Base) :
    __tablename__ = 'experiments'

    experiment_id = Column(String, primary_key = True, comment = 'pk')
    model_version_id = Column(String(255), nullable = False, comment = '모델 실험 버젼 ID')
    model_id = Column(String(255), ForeignKey('models.model_id'), nullable = False, comment = 'fk')
    parameters = Column(JSON, nullable = True, comment = 'training parameters')
    training_dataset = Column(Text, nullable = True, comment = 'training data')
    validation_dataset = Column(Text, nullable = True, comment = 'evaluation data')
    test_dataset = Column(Text, nullable = True, comment = 'test data')
    evaluations = Column(JSON, nullable = True, comment = 'eval result')
    artifact_file_paths = Column(JSON, nullable = True, comment = 'model file path')
    created_datetime = Column(DateTime(timezone = True), server_default = current_timestamp(), nullable = False)
