from mysql.connector import MySQLConnection, Error
from config import read_config

def insert_book(itemcode,name,price,quantity,date):
    query = "INSERT INTO products (itemcode, name, price, quantity, date) VALUES (%s, %s, %s, %s, %s)"

    args = (itemcode, name,price, quantity, date)
    product_id = None
    try:
        config = read_config()
        with MySQLConnection(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, args)
                product_id = cursor.lastrowid
            conn.commit()
        return product_id
    except Error as error:
        print(error)

if __name__ == '__main__':
    itemcode = input("상품 코드 입력 >>> ")  # ISBN → itemcode
    name = input("상품명을 입력하세요 >>> ")
    price = input("가격을 입력하세요 >>> ")
    quantity = input("수량을 입력하세요 >>> ")
    date = input("날짜를 입력하세요 >>> ")
    insert_book(itemcode,name,price,quantity,date)
