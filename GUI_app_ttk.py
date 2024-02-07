import random
import tkinter as tk
from tkinter import ttk

class LunchSelectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Lunch Selector")

        # 라벨 생성
        self.label = ttk.Label(master, text="메뉴를 입력하세요 :", justify="center")
        self.label.pack()

        # 메뉴 입력을 위한 Entry 위젯
        self.menu_entry = ttk.Entry(master, width=30)
        self.menu_entry.pack(pady=10)

        # 체크박스를 위한 변수들
        self.healthy_var = tk.BooleanVar()
        self.healthy_checkbox = ttk.Checkbutton(master, text="건강식만", variable=self.healthy_var)
        self.healthy_checkbox.pack()

        # 메뉴 선택 버튼
        self.select_button = ttk.Button(master, text="메뉴 결정", command=self.select_menu, width=20)
        self.select_button.pack()

        # 결과를 표시할 라벨
        self.result_label = ttk.Label(master, text="")
        self.result_label.pack()

    def select_menu(self):
        # 입력된 메뉴를 가져와서 리스트로 변환
        user_menu = self.menu_entry.get().strip()
        menu_list = [m.strip() for m in user_menu.split(',')]

        # 체크박스 상태 확인
        only_healthy = self.healthy_var.get()

        if not menu_list:
            self.result_label.config(text="메뉴가 입력되지 않았습니다.")
        else:
            # 건강식 체크 여부에 따라 메뉴 필터링
            if only_healthy:
                menu_list = [menu for menu in menu_list if "건강" in menu]

            # 랜덤으로 선택된 메뉴를 표시
            selected_menu = random.choice(menu_list)
            self.result_label.config(text=f"오늘의 점심은 {selected_menu} 어떠세요?")

if __name__ == "__main__":
    root = tk.Tk()

    # 윈도우 크기 조절
    root.geometry("400x250")

    app = LunchSelectorApp(root)
    root.mainloop()