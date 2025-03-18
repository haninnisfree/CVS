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
