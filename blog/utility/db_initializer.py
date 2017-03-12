import logging
from sqlalchemy import engine_from_config
from blog.models import basemodel
from blog.models.basemodel import (
    Session,
    Base
)

logger = logging.getLogger(__name__)


def db_initialize(settings):
    engine = engine_from_config(settings, 'sqlalchemy.')

    logger.info("Engine Configured")

    Session.configure(bind=engine)

    logger.info("Session Configured")

    Base.metadata.bind = engine

    logger.info("Base Binded to Engine ")

    Base.prepare(reflect=True)

    logger.info("DB reflected to Base")

    for k, v in Base.classes.items():
        setattr(basemodel, k, v)

    logger.info("Base tables mapped to Classes")