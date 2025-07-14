import tkinter
import customtkinter
from customtkinter import *
from tkinter import messagebox
import random


################ 참여 인원을 위한 Checkbox 위젯 ################
class MyCheckboxFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.label1 = CTkLabel(self, text="참여인원", font=(
            "Arial", 20), text_color="#FFCC70")
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.checkbox1 = CTkCheckBox(self, text="김성현")
        self.checkbox1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox2 = CTkCheckBox(self, text="김용현")
        self.checkbox2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox3 = CTkCheckBox(self, text="최승훈")
        self.checkbox3.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox4 = CTkCheckBox(self, text="하형수")
        self.checkbox4.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox5 = CTkCheckBox(self, text="우준호")
        self.checkbox5.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox6 = CTkCheckBox(self, text="지오반")
        self.checkbox6.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="w")

    def get_checked_items(self):
        checked_items = []
        for checkbox in [self.checkbox1, self.checkbox2, self.checkbox3, self.checkbox4, self.checkbox5, self.checkbox6]:
            if checkbox.get() == 1:
                checked_items.append(checkbox.cget("text"))
        return checked_items

    def get_checked_count(self):
        checked_count = 0
        for checkbox in [self.checkbox1, self.checkbox2, self.checkbox3, self.checkbox4, self.checkbox5, self.checkbox6]:
            if checkbox.get() == 1:
                checked_count += 1
        return checked_count

################ 메뉴 입력을 위한 Entry 위젯 ################


class MenuEntryFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # 라벨 생성
        self.label2 = CTkLabel(self, text="추천메뉴", font=(
            "Arial", 20), text_color="#FFCC70")
        self.label2.grid(row=0, column=1, padx=10, pady=10)

        # 메뉴 입력을 위한 Entry 위젯
        self.entry1 = CTkEntry(
            self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry1.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="w")
        self.entry2 = CTkEntry(
            self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry2.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="w")
        self.entry3 = CTkEntry(
            self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry3.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="w")
        self.entry4 = CTkEntry(
            self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry4.grid(row=4, column=1, padx=10, pady=(10, 0), sticky="w")
        self.entry5 = CTkEntry(
            self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry5.grid(row=5, column=1, padx=10, pady=(10, 0), sticky="w")
        self.entry6 = CTkEntry(
            self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry6.grid(row=6, column=1, padx=10, pady=(10, 0), sticky="w")

    def get_menu_list(self):
        menu_list = [self.entry1.get().strip(), self.entry2.get().strip(), self.entry3.get(
        ).strip(), self.entry4.get().strip(), self.entry5.get().strip(), self.entry6.get().strip()]
        return menu_list

    def get_menu_list_filt(self):
        menu_list = [self.entry1.get().strip(), self.entry2.get().strip(), self.entry3.get(
        ).strip(), self.entry4.get().strip(), self.entry5.get().strip(), self.entry6.get().strip()]
        menu_list_filt = [menu.strip() for menu in menu_list if menu.strip()]
        return menu_list_filt


class App(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.title("Lunch Selector")
        self.geometry("500x500")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # 참여 인원을 위한 Checkbox 위젯

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(
            row=0, column=0, padx=10, pady=10, sticky="nsew")

        # 메뉴 입력을 위한 Entry 위젯
        self.menu_entry_frame = MenuEntryFrame(self)
        self.menu_entry_frame.grid(
            row=0, column=1, padx=10, pady=10, sticky="nsew")

        # 메뉴 선택 버튼
        self.btn = CTkButton(self, text="메뉴 결정", command=self.select_menu)
        self.btn.grid(row=1, column=0, padx=10, pady=10,
                      sticky="ew", columnspan=2)

    def select_menu(self):
        # 체크된 항목을 가져와서 리스트로 변환
        ppl_list = self.checkbox_frame.get_checked_items()
        ppl_count = self.checkbox_frame.get_checked_count()

        # 입력된 메뉴를 가져와서 리스트로 변환
        menu_list_filt = self.menu_entry_frame.get_menu_list()
        if not menu_list_filt:
            messagebox.showerror("오류", "메뉴가 입력되지 않았습니다.")
        else:
            # 랜덤으로 선택된 메뉴를 표시
            selected_menu = random.choice(menu_list_filt)
            messagebox.showinfo(
                "결과", f"오늘의 점심은 {ppl_list}, 총 {ppl_count} 명이서 드시겠군요! 메뉴는 {selected_menu} 어떠세요?")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()
