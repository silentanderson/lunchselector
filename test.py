import random

def lunch_selector(menu_list):
    """
    주어진 메뉴 리스트 중에서 랜덤으로 하나를 선택하여 반환하는 함수
    """
    return random.choice(menu_list)

def main():
    # 사용자로부터 메뉴 입력 받기
    user_menu = input("메뉴를 입력하세요 (쉼표로 구분하여 여러 개 입력 가능): ")
    
    # 입력 받은 메뉴를 리스트로 변환
    menu = [m.strip() for m in user_menu.split(',')]

    if not menu:
        print("메뉴가 입력되지 않았습니다.")
        return

    # 랜덤으로 선택된 메뉴 출력
    selected_menu = lunch_selector(menu)
    print(f"오늘의 점심은 {selected_menu} 어떠세요?")

if __name__ == "__main__":
    main()