
"""
    Application de gestion pharmacie
    en flask python 
    Author Adama SEYE
    """
    
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # General Config
	SECRET_KEY = os.environ.get('SECRET_KEY')
	FLASK_APP = os.environ.get('FLASK_APP')
	FLASK_ENV = os.environ.get('FLASK_ENV')
	FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

	# Database
	# SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
	SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
	# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
	SQLALCHEMY_DATABASE_URI = 'sqlite:///pharmacie.db'


