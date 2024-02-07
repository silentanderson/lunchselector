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

        # 라벨 생성
        self.label = CTkLabel(self, text="참여 인원을 선택하세요 :", font=("Arial", 20), text_color="#FFCC70")
        self.label.place(relx=0.3, rely=0.1, anchor="center")

        relx1 = 0.2

        # 참여 인원을 위한 Checkbox 위젯
        self.checkbox2 = CTkCheckBox(self, text="김성현", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox2.place(relx=0.3, rely=0.2, anchor="center")
        self.checkbox2 = CTkCheckBox(self, text="김용현", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox2.place(relx=0.3, rely=0.3, anchor="center")
        self.checkbox3 = CTkCheckBox(self, text="최승훈", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox3.place(relx=0.3, rely=0.4, anchor="center")
        self.checkbox4 = CTkCheckBox(self, text="하형수", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox4.place(relx=0.3, rely=0.5, anchor="center")
        self.checkbox4 = CTkCheckBox(self, text="우준호", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox4.place(relx=0.3, rely=0.6, anchor="center")
        self.checkbox4 = CTkCheckBox(self, text="지오반", fg_color="#C850C0", checkbox_height=30, checkbox_width=30, corner_radius=10)
        self.checkbox4.place(relx=0.3, rely=0.7, anchor="center")
 

        ################ 메뉴 입력을 위한 Entry 위젯 ################
        # 라벨 생성
        self.label = CTkLabel(self, text="메뉴를 입력하세요 :", font=("Arial", 20), text_color="#FFCC70") 
        self.label.place(relx=0.7, rely=0.3, anchor="center")

        # 메뉴 입력을 위한 Entry 위젯
        self.entry = CTkEntry(self, placeholder_text="입력해주세요..", width=300, text_color="#FFCC70")
        self.entry.place(relx=0.7, rely=0.5, anchor="center")

        # 메뉴 선택 버튼
        self.btn = CTkButton(self, text="메뉴 결정하기!", command=self.select_menu, corner_radius=32, fg_color="#4158D0", hover_color="#C850C0", font=("다음_Regular", 15))
        self.btn.place(relx=0.7, rely=0.7, anchor="center")

    def select_menu(self):
        # 입력된 메뉴를 가져와서 리스트로 변환
        user_menu = self.entry.get().strip()
        menu_list = [m.strip() for m in user_menu.split(',')]
        if not menu_list:
            messagebox.showerror("오류", "메뉴가 입력되지 않았습니다.")
        else:
            # 랜덤으로 선택된 메뉴를 표시
            selected_menu = random.choice(menu_list)
            messagebox.showinfo("결과", f"오늘의 점심은 {selected_menu} 어떠세요?")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()




