import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thien20NBK06@",
        database="retail_management",
        port=3306
    )

    return connection