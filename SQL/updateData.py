from mysql.connector import MySQLConnection, Error
from config import read_config

def update_book(book_id, title):
    config = read_config()

    query = """ UPDATE products
                SET name = %s
                WHERE itemcode = %s """  # 테이블 및 컬럼명 변경

    data = (title, book_id)
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
    book_id = input("업데이트할 상품 코드(itemcode)를 입력하세요 >>> ")  # 책 번호 → 상품 코드
    new_title = input("상품의 새로운 이름을 입력하세요 >>> ")  # 책 제목 → 상품명
    affected_rows = update_book(book_id, new_title)
    print(f'Number of affected rows: {affected_rows}')
