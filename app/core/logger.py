import logging

import inject
from app.core.settings import CoreSettings


@inject.autoparams("conf")
def setup_logging(conf: CoreSettings):
    logger = logging.getLogger()
    syslog = logging.FileHandler(conf.log_file, delay=True)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(process)s] [%(levelname)s] " "[%(name)s] " "%(message)s"
    )

    syslog.setFormatter(formatter)
    logger.setLevel(getattr(logging, conf.log_level, logging.DEBUG))
    logger.addHandler(syslog)
