import tkinter
import customtkinter
from customtkinter import *
from tkinter import messagebox
import random


################ 참여 인원을 위한 Checkbox 위젯 ################
class MyCheckboxFrame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(
            self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(
            10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10,
                          pady=(10, 10), sticky="n")
            self.checkboxes.append(checkbox)

    def get_checked_items(self):
        checked_items = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_items.append(checkbox.cget("text"))
        return checked_items

    def get_checked_count(self):
        checked_count = len(self.get_checked_items())
        return checked_count

################ 메뉴 입력을 위한 Entry 위젯 ################


class MenuEntryFrame(CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.entryboxes = []

        self.title = customtkinter.CTkLabel(
            self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(
            10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            entrybox = customtkinter.CTkEntry(
                self, placeholder_text="입력해주세요..", text_color="#FFCC70")
            entrybox.grid(row=i+1, column=0, padx=10,
                          pady=(10, 10), sticky="n")
            self.entryboxes.append(entrybox)

    def get_menu_list(self):
        menu_items = [entry.get().strip() for entry in self.entryboxes]
        # 빈 문자열 제거
        menu_items_filt = [menu.strip() for menu in menu_items if menu.strip()]
        return menu_items_filt

################ 메인 앱 ################


class App(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.title("Lunch Selector")
        self.geometry("500x500")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 참여 인원을 위한 Checkbox 위젯
        checkbox_title = "참여인원"
        checkbox_texts = ["김성현", "김용현", "최승훈", "하형수", "우준호", "지오반"]
        entrybox_title = "추천메뉴"

        self.checkbox_frame = MyCheckboxFrame(
            self, checkbox_title, values=checkbox_texts)
        self.checkbox_frame.grid(
            row=0, column=0, padx=10, pady=10, sticky="ew")

        # 메뉴 입력을 위한 Entry 위젯
        self.menu_entry_frame = MenuEntryFrame(
            self, entrybox_title, values=checkbox_texts)
        self.menu_entry_frame.grid(
            row=0, column=1, padx=10, pady=10, sticky="ew")

        # 거리 입력을 위한 Slider 위젯
        self.slider = CTkSlider(self, orientation="horizontal",
                                from_=0, to=500, hover=True)
        self.slider.grid(row=1, column=0, padx=10, pady=10,
                         sticky="ew", columnspan=2)
        dist_val = self.slider.get()

        # 거리 표시 라벨
        self.distance_label = CTkLabel(
            self, text=f'거리: {dist_val} m', fg_color="gray30")
        self.distance_label.grid(
            row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        # 메뉴 선택 버튼
        self.btn = CTkButton(self, text="메뉴 결정", command=self.select_menu)
        self.btn.grid(row=3, column=0, padx=10, pady=10,
                      sticky="ew", columnspan=2)

    def select_menu(self):
        # 체크된 항목을 가져와서 리스트로 변환
        ppl_list = self.checkbox_frame.get_checked_items()
        ppl_count = self.checkbox_frame.get_checked_count()

        # 입력된 메뉴를 가져와서 리스트로 변환
        menu_list = self.menu_entry_frame.get_menu_list()
        if not menu_list:
            messagebox.showerror("오류", "메뉴가 입력되지 않았습니다.")
        else:
            # 랜덤으로 선택된 메뉴를 표시
            selected_menu = random.choice(menu_list)
            messagebox.showinfo(
                "결과", f"오늘의 점심은 {ppl_list}, 총 {ppl_count} 명이서 드시겠군요! 메뉴는 {selected_menu} 어떠세요?")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    app = App()
    app.mainloop()
