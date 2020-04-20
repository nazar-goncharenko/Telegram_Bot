import  mysql.connector;
from mysql.connector import MySQLConnection,Error
#from python_mysql_dbconfig import read_db_config


cnx = mysql.connector.connect(user='root', password='root', 
                              host='localhost', 
                              database='db_users')


if cnx.is_connected():
    print("Connected")
cnx.close()

