from loguru import logger
from sqlite3 import connect
# load self package
from .selfError import InputError
from .paraLoader import loadParameter

# load db path from parameter
class sqliteDB(object):
    def __init__(self,dbname:str) -> None:
        self.__dbPare = loadParameter()
        self.__dbStorageDir = self.__dbPare['db']['dbpath']
        self.__dbStoragePath = ''.join([self.__dbStorageDir,dbname])
        try:
            logger.debug('db path : %s'%(self.__dbStoragePath))
            self.__dbSchema = connect(self.__dbStoragePath)
        except Exception as err:
            raise err

    def __del__(self):
        logger.debug('Progream Exit')
        self.__dbSchema.commit()
        self.__dbSchema.close()

    def createObjTable(self)->bool:
        createSql = '''
        create table gitlab_accesstoken
        (id integer primary key autoincrement,
         accesstoken varchar(100) not null,
         projectname varchar(100) not null,
         createdate date not null,
         status varchar(2) default '0' not null)
        '''
        try:
            self.__dbSchema.execute(createSql)
            return True
        except Exception as err:
            raise err

    def writeDB(self,dbname:str)->bool:
        return True
        pass