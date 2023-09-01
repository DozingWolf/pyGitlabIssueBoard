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

    def dbInitial(self)->bool:
        __sysObjTableList = ['gitlab_accesstoken']
        __sysObjViewList = []
        # 循环检查表，如果不存在就初始化，并写入需要的初始化数据
        for __tableName in __sysObjTableList:
            if self.checkObjTable(tname=__tableName):
                logger.debug('Table %s is exists'%(__tableName))
            else:
                # 这里如何初始化表，需要想想
                pass

    def checkObjTable(self,tname:str)->bool:
        # 检查系统必须的表对象
        selectSql = '''
        select count(1) as count from sqlite_master where type='table' and name=?
        '''
        try:
            self.__rowData = self.__dbSchema.execute(selectSql,[tname])
            for __row in self.__rowData:
                if __row[0] == 0:
                    return False
                else:
                    return True
        except Exception as err:
            raise err

    def createObjTable_gitlab_accesstoken(self)->bool:
        # 创建表对象
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