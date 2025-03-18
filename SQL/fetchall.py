from mysql.connector import MySQLConnection, Error
from config import read_config

def query_with_fetchall():
    try:
        config = read_config()
        conn = MySQLConnection(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")  # 테이블명만 변경
        rows = cursor.fetchall()
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
        return rows
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
