from mysql.connector import MySQLConnection, Error
from config import read_config

def insert_book(title, isbn):
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"

    args = (title, isbn)
    book_id = None
    try:
        config = read_config()
        with MySQLConnection(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, args)
                book_id =  cursor.lastrowid
            conn.commit()
        return book_id
    except Error as error:
        print(error)

if __name__ == '__main__':
    title_name = input("책제목을 입력하세요 >>> ")
    isbn = input("insb번호 입력(13자리) >>> ")
    insert_book(title_name, isbn)
