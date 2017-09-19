import os
import ConfigParser

def getConfig():
    CONFIG_FILE = r'D:\pycharmprojects\myspider\ipconfig\mysqlconn\Config.cfg'
    # print os.path.join(os.getcwd(), CONFIG_FILE)
    if os.path.exists(os.path.join(os.getcwd(), CONFIG_FILE)):
        config = ConfigParser.ConfigParser()
        config.read(CONFIG_FILE)
        connKwargs = {'host': config.get('MySQL', 'mysql_host'),'port':int(config.get('MySQL', 'mysql_port')),
                      'user':config.get('MySQL', 'mysql_user'), 'passwd': config.get('MySQL', 'mysql_pwd'),
                      'db': config.get('MySQL', 'mysql_db'), 'charset': config.get('MySQL', 'mysql_charset')}
        return connKwargs