from configparser import ConfigParser

def getConnectionConf(dbname):

    cparser = ConfigParser()
    cparser.read('config/db.cnf',encoding="utf8")

    config = {
        'user': cparser.get(dbname, 'user').replace('\n',''),
        'password': cparser.get(dbname, 'password').replace('\n',''),
        'host': cparser.get(dbname, 'host').replace('\n',''),
        'database': dbname,
        'raise_on_warnings': True,
    }

    return config