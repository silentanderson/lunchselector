import tkinter as tk
from tkinter import ttk
from  tkinter import messagebox
import random

class LunchSelectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Lunch Selector")

        # 스타일 지정
        style = ttk.Style()
        style.configure("TLabel", padding=(10, 5))  # Entry 위젯의 패딩을 설정
        style.configure("TEntry", padding=(10, 5))  # Entry 위젯의 패딩을 설정
        style.configure("TButton", padding=(10, 5))  # Button 위젯의 패딩을 설정

        # 라벨 생성
        self.label = ttk.Label(master, text="메뉴를 입력하세요 :", style="TLabel", justify="center")
        self.label.pack()

        # 메뉴 입력을 위한 Entry 위젯
        self.menu_entry = ttk.Entry(master, width=30, style="TEntry")   # 스타일 적용
        self.menu_entry.pack(pady=10)

        # 메뉴 선택 버튼
        self.select_button = ttk.Button(master, text="메뉴 결정", command=self.select_menu, width=20, style="TButton")
        self.select_button.pack()

        # 결과를 표시할 라벨
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def select_menu(self):
        # 입력된 메뉴를 가져와서 리스트로 변환
        user_menu = self.menu_entry.get().strip()
        menu_list = [m.strip() for m in user_menu.split(',')]

        if not menu_list:
            self.result_label.config(text="메뉴가 입력되지 않았습니다.")
        else:
            # 랜덤으로 선택된 메뉴를 표시
            selected_menu = random.choice(menu_list)
            self.result_label.config(text=f"오늘의 점심은 {selected_menu} 어떠세요?")

if __name__ == "__main__":
    root = tk.Tk()

    # 윈도우 크기 조절
    root.geometry("400x200")

    app = LunchSelectorApp(root)
    root.mainloop()