import pw
from app import mysql
from flask_mysqldb import MySQL
import MySQLdb.cursors
"""
#DB config
app.config['MYSQL_HOST'] = pw.DBHOST
app.config['MYSQL_USER'] = pw.DBUSER
app.config['MYSQL_PASSWORD'] = pw.DBPW
app.config['MYSQL_DB'] = pw.DB

mysql = mysql
#cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
"""


def fetchQuery(sql):
    #interroga il database, ritorna un dizionario con le righe trovate
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    fetch = cursor.execute(sql)
    if fetch:
        return fetch
    else:
        return None


"""  
#Executing SQL Statements
cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
cursor.execute(''' DELETE FROM table_name WHERE condition ''')
"""


def insertQuery(table_name, column, values):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    #creazione sqlquery insert
    sql = f'INSERT INTO {table_name} ('
    for col in column:
        sql += f'{col}, '
    sql = sql.rstrip(', ')
    sql += f') VALUES('
    for val in values:
        sql += f"'{val}', "
    sql = sql.rstrip(', ')
    sql += f')'
    print(sql)
    insert = cursor.execute(sql)
    mysql.connection.commit()
    cursor.close()


def deleteQuery(table_name, id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    sql = f'DELETE FROM {table_name} WHERE id={id} '

    delete = cursor.execute(sql)
    mysql.connection.commit()
    cursor.close()


def arrfy(str):
    #convert string to arr
    arr = [str]
    return arr