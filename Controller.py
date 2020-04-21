import  mysql.connector;
from mysql.connector import MySQLConnection,Error
#from python_mysql_dbconfig import read_db_config


cnx = mysql.connector.connect(user='root', password='root', 
                              host='localhost', 
                              database='newschema')


#if cnx.is_connected():
#       cursor = cnx.cursor()
#       cursor.execute("select name from subjects;")
#       record = cursor.fetchmany(5);
#       for rec in record:
#           print(rec)

cnx.close()

