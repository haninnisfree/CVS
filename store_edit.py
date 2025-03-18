products = [
    {'product_code': 'CH001', 'product_name': '초코우유', 'price': 1500, 'quantity': 10, 'received_date': '2025-03-17'},
    {'product_code': 'CH002', 'product_name': '초코바', 'price': 1000, 'quantity': 20, 'received_date': '2025-03-17'}
]

def search_product(products):  # 상품 검색
    print("\n상품 수정")
    search_name = input("수정할 상품명: ").strip().lower()

    edit_product = []    
    found = False 

    for idx, product in enumerate(products, start=0):
        if search_name in product['product_name'].lower():
            edit_product.append(product)
            print(f"[{idx}] {product['product_name']} - {product['product_code']} - 가격: {product['price']} - 수량: {product['quantity']}")
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
            print(f"\n선택된 상품: {selected_product['product_name']}")
            print("1. 상품명")
            print("2. 상품코드")
            print("3. 가격")
            print("4. 수량")
            
            edit_choice = input("수정할 항목 번호: ")
            
            if edit_choice == '1':
                selected_product['product_name'] = input("새 상품명: ")
            elif edit_choice == '2':
                selected_product['product_code'] = input("새 상품코드: ")
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

# 수정 전 출력
print("수정 전:", products)

# 검색 결과 저장 후 수정
edit_products = search_product(products)  # 반환값을 변수에 저장
edit_product_detail(edit_products)  # 저장된 변수를 전달

# 수정 후 출력
print("수정 후:", products)