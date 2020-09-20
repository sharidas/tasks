"""
Configuration for the flask app
"""
class Config:
    """
    The base configuration file
    """
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:secret@postgresdb:5432/postgres")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD=True

class ProductionConfig(Config):
    """
    Production config
    """
    DEBUG = False
    TESTING = False
    SAVE_DATA_API_KEY = "LETS_SAVE_WORLD_123456"

class DevelopmentConfig(Config):
    """
    Development config
    """
    DEBUG = True
    TESTING = True
    SAVE_DATA_API_KEY = "LETS_SAVE_WORLD_123456"


class TestingConfig(Config):
    """
    Test configuration
    """
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://sujith:sujith123@localhost:5432/testdb"
    )
    DEBUG = False
    TESTING = True
    SAVE_DATA_API_KEY = "LETS_SAVE_WORLD_123456"
