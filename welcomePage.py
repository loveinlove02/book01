import tkinter as tk
import assets as asset
from PIL import Image, ImageTk

import selectPage
import returnPage

import webbrowser

class WelcomePage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.asstes = asset.Assets()
        self.create_widgets()

    def create_widgets(self):
        self.welcome_page_fm = tk.Frame(self, highlightbackground='#314159', highlightthickness=2, bg='#FFFFFF')
        self.welcome_page_fm.pack(pady=0)
        self.welcome_page_fm.configure(width=890, height=780)


        self.title_frame = tk.Frame(self.welcome_page_fm, bg='#E4E724')
        self.title_frame.place(x=0, y=0)
        self.title_frame.configure(width=885, height=45)

        self.title_lable = tk.Label(self.welcome_page_fm, text= '무인 도서 대출 & 반납기', font='궁서 23 bold', fg='#004BE5', bg='#FFFFFF')
        self.title_lable.place(x=280, y=70)

        logo = Image.open('images/chatbot.png')
        resized_image_logo = logo.resize((200, 150), Image.LANCZOS)
        self.book_logo = ImageTk.PhotoImage(resized_image_logo)

        self.center_logo_button = tk.Button(self.welcome_page_fm, image=self.book_logo, bg='#FFFFFF', bd=0, command=self.open_browser)
        self.center_logo_button.place(x=340, y=150)

        self.explain_lb_three = tk.Label(self.welcome_page_fm, text='챗봇 / Chatbot', font='궁서 20', fg='#004BE5', bg='white')
        self.explain_lb_three.place(x=330, y=320)


        # self.center_logo_label = tk.Label(self.welcome_page_fm, image=self.book_logo, bg='#FFFFFF')
        # self.center_logo_label.place(x=340, y=190)

        self.bottom_frame = tk.Frame(self.welcome_page_fm, bg='white')
        self.bottom_frame.place(x=0, y=420)
        self.bottom_frame.configure(width=885, height=340)



        book1 = Image.open('images/loan.png')
        book2 = Image.open('images/return.png')

        # 이미지 resize
        resized_image_book1 = book1.resize((250, 200), Image.LANCZOS)
        resized_image_book2 = book2.resize((250, 200), Image.LANCZOS)

        # tkinter에서 사용할 수 있는 형식으로 변환
        self.book_logo1 = ImageTk.PhotoImage(resized_image_book1)
        self.book_logo2 = ImageTk.PhotoImage(resized_image_book2)

        self.borrow_btn = tk.Button(self.bottom_frame, image=self.book_logo1, bg='white', bd=0, command=self.forwad_to_borrow_page)
        self.borrow_btn.place(x=150, y=0)

        self.return_btn = tk.Button(self.bottom_frame, image=self.book_logo2, bg='white', bd=0, command=self.forwad_to_return_page)
        self.return_btn .place(x=480, y=0)

        self.borrow_label = tk.Label(self.bottom_frame, text= '대출 / Loan', font='궁서 20', fg='#004BE5', bg='white')
        self.borrow_label.place(x=200, y=245)

        self.return_label = tk.Label(self.bottom_frame, text= '반납 / Return', font='궁서 20', fg='#004BE5', bg='white')
        self.return_label.place(x=510, y=245)

        self.creator_lb = tk.Label(self.bottom_frame, text='Creator : 이무겸', font='궁서 10 bold', fg='#000000', bg='white')
        self.creator_lb.place(x=770, y=320)

    def forwad_to_borrow_page(self):
        self.welcome_page_fm.destroy()
        self.update()

        select_page_fm = selectPage.SelectPage(self)
        select_page_fm.pack()

    def forwad_to_return_page(self):
        self.welcome_page_fm.destroy()
        self.update()

        retrun_page_fm = returnPage.ReturnPage(self)
        retrun_page_fm.pack()


    def open_browser(self):
        url = 'http://localhost:8501/'
        webbrowser.open(url)
















# https://www.flaticon.com/kr/free-icon/book_2232688
# https://littledeep.com/book-illustration-free-download/