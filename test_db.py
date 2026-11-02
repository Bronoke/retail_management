from database import get_connection

try:
    conn = get_connection()
    print("KET NOI MYSQL THANH CONG!")

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")

    for table in cursor.fetchall():
        print(table)

    cursor.close()
    conn.close()

except Exception as e:
    print("LOI KET NOI:", e)