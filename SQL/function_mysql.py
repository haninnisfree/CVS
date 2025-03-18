from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser

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

def connect(): 
    conn = None
    try: 
        config = read_config()
        conn = MySQLConnection(**config)
    except Error as error:
        print(error)
    return conn

def query_with_fetchall(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")  # 테이블명 변경
    rows = cursor.fetchall()
    print('Total Row(s):', cursor.rowcount)
    for row in rows:
        print(row)
    return rows

def insert_product(conn, itemcode, name, price, quantity, date):
    query = "INSERT INTO products (itemcode, name, price, quantity, date) VALUES (%s, %s, %s, %s, %s)"
    args = (itemcode, name, price, quantity, date)
    product_id = None
    with conn.cursor() as cursor:
        cursor.execute(query, args)
        product_id = cursor.lastrowid
    conn.commit()
    return product_id

def update_product(conn, itemcode, name, price, quantity, date):
    query = """ UPDATE products
                SET name = %s
                WHERE itemcode = %s """  # 테이블명 및 컬럼명 변경
    data = (itemcode, name, price, quantity, date)
    affected_rows = 0 
    with conn.cursor() as cursor:
        cursor.execute(query, data)
        affected_rows = cursor.rowcount
    conn.commit()
    return affected_rows 

def delete_product(conn, itemcode, name, price, quantity, date):
    query = "DELETE FROM products WHERE itemcode = %s"  # 테이블명 및 컬럼명 변경
    data = (itemcode, ) 
    affected_rows = 0  
    with conn.cursor() as cursor:
        cursor.execute(query, data)
        affected_rows = cursor.rowcount  # 삭제된 행 수 저장
    conn.commit()
    return affected_rows  

if __name__ == '__main__':
    conn = connect()
    if conn:
        print("=== 현재 상품 목록 ===")
        query_with_fetchall(conn)

        print("\n=== 상품 추가 ===")
        title_name = input("상품명을 입력하세요 >>> ")  
        itemcode = input("상품 코드 입력 >>> ")  
        insert_product(conn, title_name, itemcode)
        query_with_fetchall(conn)

        print("\n=== 상품 업데이트 ===")
        itemcode = input("업데이트할 상품의 코드(itemcode)를 입력하세요 >>> ")
        new_name = input("상품의 새로운 이름을 입력하세요 >>> ")
        affected_rows = update_product(conn, itemcode, new_name)
        print(f'Number of affected rows: {affected_rows}')
        query_with_fetchall(conn)

        print("\n=== 상품 삭제 ===")
        itemcode = input("삭제할 상품 코드(itemcode)를 입력하세요 >>> ")
        affected_rows = delete_product(conn, itemcode)
        print(f'Number of affected rows: {affected_rows}')
        query_with_fetchall(conn)

        conn.close()
