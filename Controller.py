import  mysql.connector;

cnx = mysql.connector.connect(user='root', password='root', 
                              host='localhost', 
                              database='db_users')

cnx.close()

