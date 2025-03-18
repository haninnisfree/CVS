from mysql.connector import MySQLConnection, Error
from config import read_config

def delete_product(itemcode):
    config = read_config()
    query = "DELETE FROM products WHERE itemcode = %s"
    data = (itemcode,) 
    affected_rows = 0  

    try:
        with MySQLConnection(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, data)
                affected_rows = cursor.rowcount
            conn.commit()
    except Error as error:
        print(error)

    return affected_rows  

if __name__ == '__main__':
    itemcode = input("삭제할 상품 코드(itemcode)를 입력하세요 >>> ")  
    affected_rows = delete_product(itemcode)
    print(f'Number of affected rows: {affected_rows}')
