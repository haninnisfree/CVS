import sys

# 예제 데이터: 상품명, 상품코드, 가격, 받아온 날짜, 재고량
items = [
    ["콜라", "A001", 1500, "2025-03-01", 10],
    ["사이다", "A002", 1400, "2025-03-02", 5],
    ["초코바", "A003", 1200, "2025-03-03", 7]
]

# 상품 삭제 기능
def delete_item():
    print("\n[ 상품 삭제 ]")
    name = input('삭제할 상품의 상품명을 입력하세요 >>> ')
    
    # 입력한 상품명과 일치하는 상품 찾기
    found_items = [item for item in items if item[0] == name] 
    
    if not found_items:
        print("해당하는 상품이 없습니다.")
        return
    
    # 찾은 상품 목록 출력
    for index, item in enumerate(found_items, start=1):
        print(f'{index}. {item}')
    
    # 삭제할 상품 선택
    choice = int(input("삭제할 상품의 번호를 입력하세요 >>> "))
    if 1 <= choice <= len(found_items):
        items.remove(found_items[choice - 1])
        print("삭제 완료.")
    else:
        print("잘못된 입력입니다.")

# 상품 목록 조회 기능
def list_items():
    print("\n[ 상품 목록 보기 ]")
    search_name = input("검색할 상품명을 입력하세요 (전체 목록을 보려면 Enter) >>> ")
    
    # 입력한 상품명이 포함된 상품 필터링 (전체 목록 조회 가능)
    filtered_items = [item for item in items if search_name in item[0]] if search_name else items
    
    if not filtered_items:
        print("해당하는 상품이 없습니다.")
        return
    
    # 상품 목록 출력
    print("-" * 60)
    for item in filtered_items:
        print(f'{item[0]} / {item[1]} / {item[2]}원 / {item[3]} / 재고: {item[4]}')
    print("-" * 60)

# 프로그램 종료 기능
def exit_program():
    print("\n[ 프로그램 종료 ]")
    sys.exit()
