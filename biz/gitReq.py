from requests import get,post
from loguru import logger

class gitlabReqStru(object):
    def __init__(self,pat,rurl) -> None:
        self.__gitlabPersonAlaccessToken = pat
        self.__reqHeader = {'PRIVATE-TOKEN':self.__gitlabPersonAlaccessToken}
        self.rootUrl = rurl

    def createIssue(isu:str) -> bool:
        pass

    def checkAllIssue() -> bool:
        pass