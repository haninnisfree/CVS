from mysql.connector import MySQLConnection, Error
from config import read_config

def update_product(itemcode, name):
    config = read_config()

    query = """ UPDATE products
                SET name = %s
                WHERE itemcode = %s """  

    data = (name, itemcode)
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
    id = input("업데이트할 상품 코드(itemcode)를 입력하세요 >>> ")  
    new_title = input("상품의 새로운 이름을 입력하세요 >>> ") 
    affected_rows = update_product(id, new_title)
    print(f'Number of affected rows: {affected_rows}')
