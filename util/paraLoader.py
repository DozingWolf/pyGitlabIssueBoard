from loguru import logger
from configparser import ConfigParser
from . import paraLocalPath

def loadParameter():
    try:
        # logger.debug(paraLocalPath)
        paraSet = ConfigParser()
        paraSet.read(filenames=paraLocalPath)
        # logger.debug(paraSet)
    except Exception as err:
        raise err
    return paraSet
