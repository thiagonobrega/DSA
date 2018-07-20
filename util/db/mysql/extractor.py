
import mysql.connector

from py2neo import Graph
from model.infra import TableCollation, TableType, TableEngine, Table, DataBase
from util.db import base


def getConnection():
    config = base.getConnectionConf("mysql")
    cnx = mysql.connector.connect(**config)
    return cnx

def getDatabases(cnx):
    cursor = cnx.cursor()
    cursor.execute("SHOW DATABASES")
    databases = []

    for i in cursor:
        dbt = i[0]  # .decode("utf-8")
        databases.append(dbt)

    databases.remove('information_schema')
    databases.remove('mysql')
    databases.remove('performance_schema')
    return databases

def addCollection(cnx,g,cname):
    dbc = TableCollation(cname)
    z = TableCollation.match(g, cname)
    zbc = z.first()

    if zbc is None:
        graph.push(dbc)
        return dbc
    else:
        return zbc

def addType(cnx,g,tipo):
    dbc = TableType(tipo)
    z = TableType.match(g, tipo)
    zbc = z.first()

    if zbc is None:
        graph.push(dbc)
        return dbc
    else:
        return zbc

def addEngine(cnx,g,tipo):
    dbc = TableEngine(tipo)
    z = TableEngine.match(g, tipo)
    zbc = z.first()

    if zbc is None:
        graph.push(dbc)
        return dbc
    else:
        return zbc

def addTable(cnx,g,name):
    dbc = Table(name)
    return dbc

def getDatabaseTables(cnx,database_name,graph):
    cursor = cnx.cursor()
    sql = "SELECT TABLE_SCHEMA,TABLE_NAME,ENGINE,TABLE_TYPE,TABLE_COLLATION FROM information_schema.TABLES " \
          "WHERE TABLE_SCHEMA = \'"+database_name+"\';"
    cursor.execute(sql)

    db = DataBase(database_name)

    for i in cursor:
        collation = addCollection(cnx, graph, i[4])
        typ = addType(cnx, graph, i[3])
        eng = addEngine(cnx, graph, i[2])
        table = addTable(cnx, graph, i[1])

        table.set_Collation(collation)
        table.set_Engine(eng)
        table.set_Type(typ)
        #print(i[1])
        graph.push(table)
        db.add_Table(table)

        # graph.merge(table)
        # graph.merge(typ)
        # graph.merge(eng)
        # graph.merge(collation)

    graph.merge(db)



graph = Graph(auth=('neo4j', ''))
graph.delete_all()
cnx = getConnection()
#getDatabaseTables(cnx,'COMVEST',graph)
#getDatabaseTables(cnx,'ControleAcademico',graph)

#>>> graph.run("MATCH (a:Person) RETURN a.name, a.born LIMIT 4").data()

#getDatabaseTables(cnx,'ControleAcademico',graph)

for db in getDatabases(cnx):
    getDatabaseTables(cnx,db,graph)
    print("\t Done >> " + db)

cnx.close()
