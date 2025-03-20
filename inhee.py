import sys
from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser
import os
os.chdir("C:/gitproject/pythonproject/CVS/SQL")

# 데이터베이스 설정 불러오기
def read_config(filename='app.ini', section='mysql'):    
    config = ConfigParser()
    config.read(filename)
    data = {}
    if config.has_section(section):
        items = config.items(section)
        for item in items:
            data[item[0]] = item[1]
    else:
        raise Exception(f'{section} section not found in the {filename} file')
    return data

# MySQL 연결
def connect(): 
    try: 
        config = read_config()
        return MySQLConnection(**config)
    except Error as error:
        print(error)
        return None

# 상품 등록 (MySQL 데이터 삽입)
def insert_product(conn):
    itemcode = input("상품 코드 입력 >>> ").strip()
    name = input("상품명 입력 >>> ").strip()
    price = int(input("가격 입력 >>> "))
    quantity = int(input("수량 입력 >>> "))
    date = input("입고 날짜 (예: 2025-03-17) >>> ").strip()

    query = """INSERT INTO products (itemcode, name, price, quantity, date)
               VALUES (%s, %s, %s, %s, %s)
               ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity)"""
    args = (itemcode, name, price, quantity, date)

    try:
        with conn.cursor() as cursor:
            cursor.execute(query, args)
            conn.commit()
            print("상품이 등록되었습니다.")
    except Error as error:
        print(f"오류 발생: {error}")

# 상품 수정 (MySQL 데이터 업데이트)
def update_product(conn):
    itemcode = input("업데이트할 상품 코드 입력 >>> ").strip()
    
    query_check = "SELECT * FROM products WHERE itemcode = %s"
    with conn.cursor() as cursor:
        cursor.execute(query_check, (itemcode,))
        product = cursor.fetchone()

    if not product:
        print("해당 상품이 존재하지 않습니다.")
        return

    print("수정할 항목을 선택하세요:")
    print("1. 상품명")
    print("2. 가격")
    print("3. 수량")

    choice = input("수정할 항목 번호 >>> ").strip()
    
    if choice == '1':
        new_value = input("새로운 상품명 입력 >>> ").strip()
        query = "UPDATE products SET name = %s WHERE itemcode = %s"
    elif choice == '2':
        new_value = int(input("새로운 가격 입력 >>> "))
        query = "UPDATE products SET price = %s WHERE itemcode = %s"
    elif choice == '3':
        new_value = int(input("새로운 수량 입력 >>> "))
        query = "UPDATE products SET quantity = %s WHERE itemcode = %s"
    else:
        print("잘못된 입력입니다.")
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (new_value, itemcode))
            conn.commit()
            print("상품이 업데이트되었습니다.")
    except Error as error:
        print(f"오류 발생: {error}")

# 상품 삭제 (MySQL 데이터 삭제)
def delete_product(conn):
    itemcode = input("삭제할 상품 코드 입력 >>> ").strip()

    query_check = "SELECT * FROM products WHERE itemcode = %s"
    with conn.cursor() as cursor:
        cursor.execute(query_check, (itemcode,))
        product = cursor.fetchone()

    if not product:
        print("해당 상품이 존재하지 않습니다.")
        return

    confirm = input(f"정말 '{product[1]}' 상품을 삭제하시겠습니까? (y/n): ").strip().lower()
    if confirm == 'y':
        query = "DELETE FROM products WHERE itemcode = %s"
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, (itemcode,))
                conn.commit()
                print("상품이 삭제되었습니다.")
        except Error as error:
            print(f"오류 발생: {error}")
    else:
        print("삭제가 취소되었습니다.")

# 상품 목록 조회 (MySQL 데이터 조회)
def query_with_fetchall(conn):
    search_name = input("검색할 상품명 (전체 목록 조회: Enter) >>> ").strip()

    query = "SELECT * FROM products"
    args = ()
    if search_name:
        query += " WHERE name LIKE %s"
        args = ('%' + search_name + '%',)

    try:
        with conn.cursor() as cursor:
            cursor.execute(query, args)
            rows = cursor.fetchall()
            if rows:
                print("\n=== 상품 목록 ===")
                for row in rows:
                    print(f"코드: {row[0]}, 상품명: {row[1]}, 가격: {row[2]}, 수량: {row[3]}, 날짜: {row[4]}")
            else:
                print("해당 상품이 없습니다.")
    except Error as error:
        print(f"오류 발생: {error}")

# CLI 메뉴 화면
display = '''
┌==================================================┐
1. 상품 등록  2. 상품 수정 3. 상품 삭제 4. 상품 목록  5. 종료
└==================================================┘
메뉴 번호를 선택해주세요 >>> '''

# 메인 실행 로직
if __name__ == '__main__':
    conn = connect()
    if not conn:
        print("데이터베이스 연결에 실패했습니다. 프로그램을 종료합니다.")
        sys.exit()

    while True:
        menu = input(display).strip()

        if menu == '1':  # 상품 등록
            insert_product(conn)

        elif menu == '2':  # 상품 수정
            update_product(conn)

        elif menu == '3':  # 상품 삭제
            delete_product(conn)

        elif menu == '4':  # 상품 목록 조회
            query_with_fetchall(conn)

        elif menu == '5':  # 프로그램 종료
            print("프로그램 종료")
            conn.close()
            sys.exit()

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
