from mysql.connector import MySQLConnection, Error
from config import read_config

def insert_book(title, isbn):
    query = "INSERT INTO products(name, itemcode) " \  # 테이블명 및 컬럼명 변경
            "VALUES(%s,%s)"

    args = (title, isbn)
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
    title_name = input("상품명을 입력하세요 >>> ")  # 책제목 → 상품명
    itemcode = input("상품 코드 입력 >>> ")  # ISBN → itemcode
    insert_book(title_name, itemcode)
