# -*- coding : utf-8 -*-

import ConfigParser

CONFIG_FILE = "Config.cfg"
MYSQL_HOST = "127.0.0.1"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PWD = "111111"
MYSQL_DB = "spider"
MYSQL_CHARSET= "utf8"

if __name__ == "__main__":
    conf = ConfigParser.ConfigParser()
    configfile = open(CONFIG_FILE,'w')
    conf.add_section('MySQL')

    conf.set('MySQL','MYSQL_HOST',MYSQL_HOST)
    conf.set('MySQL','MYSQL_PORT',MYSQL_PORT)
    conf.set('MySQL','MYSQL_USER',MYSQL_USER)
    conf.set('MySQL','MYSQL_PWD',MYSQL_PWD)
    conf.set('MySQL','MYSQL_DB',MYSQL_DB)
    conf.set('MySQL', 'MYSQL_CHARSET', MYSQL_CHARSET)

    conf.write(configfile)
    configfile.close()
