import sys

display = '''
┌==================================================┐
1. 상품등록  2. 상품수정 3. 상품삭제 4. 상품목록  5.종료
└==================================================┘
메뉴 번호를 선택해주세요 >>> '''

products = [
    {'itemcode': 'CH001', 'name': '초코우유', 'price': 1500, 'quantity': 10, 'date': '2025-03-17'}, 
    {'itemcode': 'CH002', 'name': '초코바', 'price': 1000, 'quantity': 20, 'date': '2025-03-17'}, 
    {'itemcode': 'CH003', 'name': '초코파이', 'price': 2000, 'quantity': 15, 'date': '2025-03-17'},
    {'itemcode': 'CH004', 'name': '초코케이크', 'price': 2500, 'quantity': 5, 'date': '2025-03-17'},
    {'itemcode': 'CH005', 'name': '초코칩쿠키', 'price': 3000, 'quantity': 30, 'date': '2025-03-17'},
    {'itemcode': 'CH006', 'name': '초코팝콘', 'price': 3500, 'quantity': 25, 'date': '2025-03-17'},
    {'itemcode': 'CH007', 'name': '초코빵', 'price': 4000, 'quantity': 10, 'date': '2025-03-17'},
    {'itemcode': 'CH008', 'name': '초코케이크', 'price': 4500, 'quantity': 20, 'date': '2025-03-17'},
    {'itemcode': 'CH009', 'name': '초코칩쿠키', 'price': 5000, 'quantity': 15, 'date': '2025-03-17'},
    {'itemcode': 'CH010', 'name': '초코팝콘', 'price': 5500, 'quantity': 5, 'date': '2025-03-17'}
]


def register_product():
    product_name = input("상품명: ")
    product_code = input("상품코드: ")
    price = int(input("가격: "))
    quantity = int(input("수량: "))
    received_date = input("입고 날짜 (예: 2025-03-17): ") 
    
    for product in products:
        if product['itemcode'] == product_code and product['date'] == received_date:
            product['quantity'] += quantity  # 동일 날짜면 수량만 증가
            print("기존 상품 수량이 업데이트되었습니다.")
            return
    
    new_product = {
        'itemcode': product_code,
        'name': product_name,
        'price': price,
        'quantity': quantity,
        'date': received_date
    }
    products.append(new_product)
    print("새 상품이 등록되었습니다.")

def search_product(products):  # 상품 검색
    print("\n상품 수정")
    search_name = input("수정할 상품명: ").strip().lower()
    edit_product = []    
    found = False 
    for idx, product in enumerate(products, start=0):
        if search_name in product['name'].lower():
            edit_product.append(product)
            print(f"[{idx}] {product['name']} - {product['itemcode']} - 가격: {product['price']} - 수량: {product['quantity']}")
            found = True
    if not found:
        print("해당 상품이 없습니다.")
    return edit_product

def edit_product_detail(edit_product):  # 상품 수정
    if not edit_product:
        return
    
    try:
        choice = int(input("수정할 상품 번호: "))
        if 0 <= choice < len(edit_product):  # products 대신 edit_product 길이 체크
            selected_product = edit_product[choice]
            print(f"\n선택된 상품: {selected_product['name']}")  # 'product_name' -> 'name'으로 수정
            print("1. 상품명")
            print("2. 상품코드")
            print("3. 가격")
            print("4. 수량")
            
            edit_choice = input("수정할 항목 번호: ")
            
            if edit_choice == '1':
                selected_product['name'] = input("새 상품명: ")
            elif edit_choice == '2':
                selected_product['itemcode'] = input("새 상품코드: ")
            elif edit_choice == '3':
                selected_product['price'] = int(input("새 가격: "))
            elif edit_choice == '4':
                selected_product['quantity'] = int(input("새 수량: "))
            else:
                print("잘못된 항목 번호입니다.")
                return
            
            print("수정이 완료되었습니다.")
        else:
            print("잘못된 상품 번호입니다.")
    except ValueError:
        print("숫자를 입력해주세요.")
    
def search_product02(products):  # 상품 검색
    print("\n상품 목록")
    search_name = input("검색할 상품명 (전체 목록은 Enter): ").strip().lower()
    edit_product = []    
    found = False 
    
    if search_name == "":  # 엔터만 누른 경우
        for idx, product in enumerate(products, start=0):
            edit_product.append(product)
            print(f"[{idx}] {product['name']} - {product['itemcode']} - 가격: {product['price']} - 수량: {product['quantity']}")
            found = True
    else:  # 검색어가 있는 경우
        for idx, product in enumerate(products, start=0):
            if search_name in product['name'].lower():
                edit_product.append(product)
                print(f"[{idx}] {product['name']} - {product['itemcode']} - 가격: {product['price']} - 수량: {product['quantity']}")
                found = True
    
    if not found:
        print("해당 상품이 없습니다.")
    

while True:
    menu = input(display).strip()

    if menu == '1': # 상품등록
        register_product()

    elif menu == '2':  # 상품수정
        edit_product = search_product(products)
        edit_product_detail(edit_product)

    elif menu == '3': # 상품삭제
        pass

    elif menu == '4': # 상품목록
        search_product02(products)

    elif menu == '5':
        print('프로그램 종료')
        sys.exit()

    else:
        print("메뉴 선택을 잘못하셨습니다.")