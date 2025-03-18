display = '''
┌==================================================┐
1. 상품등록  2. 상품수정 3. 상품삭제 4. 상품목록  5.종료
└==================================================┘
메뉴 번호를 선택해주세요 >>> '''

products = []

while True:
    menu = input(display).strip()

    if menu == '1':

        def add_product(self):
            name = input("상품명을 입력하세요: ")
            itemcode = input("상품코드를 입력하세요: ")
            price = int(input("가격을 입력하세요: "))
            date = input("받아온 날짜를 입력하세요 (YYYY-MM-DD): ")
            quantity = int(input("수량을 입력하세요: "))

            if itemcode in self.products:
                self.products[itemcode]['quantity'] += quantity
            else:
                self.products[itemcode] = {
                    'name': name,
                    'price': price,
                    'date': date,
                    'quantity': quantity
                }
            print("상품이 등록되었습니다!")



def search_and_delete(items, search_name):
    # 동일한 이름의 상품을 찾음
    found_items = [item for item in items if item["name"] == search_name]

    if not found_items:
        print(f"'{search_name}' 상품을 찾을 수 없습니다.")
        return

    # 동일한 이름의 상품이 여러 개일 경우 선택하도록 함
    if len(found_items) > 1:
        print(f"'{search_name}' 상품이 여러 개 있습니다. 삭제할 상품을 선택하세요.")
        for idx, item in enumerate(found_items):
            print(f"{idx + 1}. 상품명: {item['name']}, 가격: {item['price']}원, 수량: {item['quantity']}개, 반입날짜: {item['date']}")
        
        choice = int(input("삭제할 상품의 번호를 입력하세요: ")) - 1

        if choice < 0 or choice >= len(found_items):
            print("잘못된 번호입니다.")
            return

        selected_item = found_items[choice]
    else:
        selected_item = found_items[0]

    # 삭제 확인
    confirm = input(f"정말 '{selected_item['name']}' 상품을 삭제하시겠습니까? (y/n): ").strip().lower()

    if confirm == 'y':
        items.remove(selected_item)
        print(f"상품 '{selected_item['name']}'이(가) 삭제되었습니다.")
    else:
        print("삭제가 취소되었습니다.")

# 상품 삭제 테스트
search_name = input("삭제할 상품명을 입력하세요: ").strip()
search_and_delete(items, search_name)