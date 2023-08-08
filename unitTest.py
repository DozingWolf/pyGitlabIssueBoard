from loguru import logger
# self package
from util.paraLoader import loadParameter
from util.optSqlite import sqliteDB

if __name__ == '__main__':
    logger.debug('# TEST 1')
    para = loadParameter()
    logger.debug(para['db']['dbpath'])

    logger.debug('# TEST 2')
    db = sqliteDB(dbname='Gitlab-issue.db')
    if db.checkObjTable(tname='gitlab_accesstoken'):
        logger.debug('table exists')
    else:
        db.createObjTable()
