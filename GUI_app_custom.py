import tkinter
import customtkinter
from customtkinter import *
from tkinter import messagebox
import random

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.title("Lunch Selector")
        self.geometry("800x500")

        ################ 참여 인원을 위한 Checkbox 위젯 ################

        relx_check = 0.2
        relx_entry = 0.5
        relx_button = 0.8

        # 라벨 생성
        self.label = CTkLabel(self, text="인원을 선택하세요 :", font=("Arial", 20), text_color="#FFCC70")
        self.label.place(relx=relx_check, rely=0.1, anchor="center")

        # 참여 인원을 위한 Checkbox 위젯
        check_var = tkinter.BooleanVar()

        self.checkbox1 = CTkCheckBox(self, text="김성현", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox1.place(relx=relx_check, rely=0.2, anchor="center")
        self.checkbox2 = CTkCheckBox(self, text="김용현", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox2.place(relx=relx_check, rely=0.3, anchor="center")
        self.checkbox3 = CTkCheckBox(self, text="최승훈", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox3.place(relx=relx_check, rely=0.4, anchor="center")
        self.checkbox4 = CTkCheckBox(self, text="하형수", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox4.place(relx=relx_check, rely=0.5, anchor="center")
        self.checkbox5 = CTkCheckBox(self, text="우준호", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox5.place(relx=relx_check, rely=0.6, anchor="center")
        self.checkbox6 = CTkCheckBox(self, text="지오반", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox6.place(relx=relx_check, rely=0.7, anchor="center")
 

        ################ 메뉴 입력을 위한 Entry 위젯 ################
        # 라벨 생성
        self.label = CTkLabel(self, text="메뉴를 입력하세요 :", font=("Arial", 20), text_color="#FFCC70") 
        self.label.place(relx=relx_entry, rely=0.1, anchor="center")

        # 메뉴 입력을 위한 Entry 위젯
        self.entry1 = CTkEntry(self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry1.place(relx=relx_entry, rely=0.2, anchor="center")
        self.entry2 = CTkEntry(self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry2.place(relx=relx_entry, rely=0.3, anchor="center")
        self.entry3 = CTkEntry(self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry3.place(relx=relx_entry, rely=0.4, anchor="center")
        self.entry4 = CTkEntry(self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry4.place(relx=relx_entry, rely=0.5, anchor="center")
        self.entry5 = CTkEntry(self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry5.place(relx=relx_entry, rely=0.6, anchor="center")
        self.entry6 = CTkEntry(self, placeholder_text="입력해주세요..", width=100, text_color="#FFCC70")
        self.entry6.place(relx=relx_entry, rely=0.7, anchor="center")

        # 메뉴 선택 버튼
        self.btn = CTkButton(self, text="메뉴 결정하기!", command=self.select_menu, corner_radius=32, fg_color="#4158D0", hover_color="#C850C0", font=("다음_Regular", 15))
        self.btn.place(relx=relx_button, rely=0.45, anchor="center")

    def select_menu(self):
       
        # 선택된 인원을 가져와서 리스트로 변환
        checkbox_list = [self.checkbox1, self.checkbox2, self.checkbox3, self.checkbox4, self.checkbox5, self.checkbox6]
        ppl_list = []
        ppl_count = 0  
        for checkbox in checkbox_list:
            if checkbox.get() == 1:
                ppl_list.append(checkbox.cget("text"))
                ppl_count += 1

        # 입력된 메뉴를 가져와서 리스트로 변환
        menu_list = [self.entry1.get().strip(), self.entry2.get().strip(), self.entry3.get().strip(), self.entry4.get().strip(), self.entry5.get().strip(), self.entry6.get().strip()]
        menu_list_filt = [menu.strip() for menu in menu_list if menu.strip()]
        if not menu_list:
            messagebox.showerror("오류", "메뉴가 입력되지 않았습니다.")
        else:
            # 랜덤으로 선택된 메뉴를 표시
            selected_menu = random.choice(menu_list_filt)
            messagebox.showinfo("결과", f"오늘의 점심은 {ppl_list}, 총 {ppl_count} 명이서 드시겠군요! 메뉴는 {selected_menu} 어떠세요?")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()




