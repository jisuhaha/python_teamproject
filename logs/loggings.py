import logging
import logging.config
import os

config_path = os.path.join(os.path.dirname(__file__), '../logs/logging.conf')
logging.config.fileConfig(config_path)
logger = logging.getLogger()

if __name__ == '__main__' :
    logger.debug('debug...')
    logger.info('info...')
    logger.warning('warning...')
    logger.error('error...')
    logger.critical('critical...')
    