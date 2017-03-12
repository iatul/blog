#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Main entry point
"""

import logging
from pyramid.config import Configurator

from blog.common import saved_ini
from blog.utility.db_initializer import db_initialize

logger = logging.getLogger(__name__)

def main(global_config, **settings):

    db_initialize(settings)
    logger.info('DB initialization complete')

    saved_ini.ini_settings = settings  # saving ini  settings so that it can be used anywhere

    logger.info('ini settings saved')

    config = Configurator(settings=settings)
    config.include('cornice')
    config.scan('blog.views')
    return config.make_wsgi_app()