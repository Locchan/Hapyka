import sqlalchemy.exc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from __main__ import config_provider

from hapyka.utils.logger import get_logger

db_login = config_provider.get("database_login")
db_password = config_provider.get("database_password")
db_schema = config_provider.get("database_schema")
db_address = config_provider.get("database_address")
db_port = config_provider.get("database_port")

logger = get_logger()


engine = None
Base = None
session_generator = None
path = ""


def initialize():
    global engine, Base, session_generator
    try:
        logger.info("Initializing database: {}@{}:{}/{}...".format(db_login, db_address, db_port, db_schema))
        engine = create_engine('mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(db_login, db_password, db_address,
                                                                              db_port, db_schema))
        Base = declarative_base()
        session_generator = scoped_session(sessionmaker(bind=engine, autocommit=True))
        import hapyka.database.models
        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized")
    except Exception as e:
        logger.error("Could not initialize: {}".format(e.__class__.__name__))
        raise e


def get_session_factory():
    return session_generator


def get_connection():
    return engine.connect()


def get_raw_connection():
    return engine.raw_connection()


def get_session():
    return session_generator()


def get_transaction():
    session = get_session()
    try:
        session_transaction = session.begin()
    except sqlalchemy.exc.InvalidRequestError:
        session_transaction = session.begin_nested()
    if session_transaction is None:
        raise sqlalchemy.exc.InvalidRequestError("Could not create an sqlite session.")
    return session, session_transaction
