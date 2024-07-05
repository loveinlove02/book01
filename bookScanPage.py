import tkinter as tk
from PIL import Image, ImageTk
import cv2

import welcomePage
import firebaseDB

import assets as asset

class BookScanPage(tk.Frame):
    def __init__(self, container, id):
        super().__init__(container)

        self.user_id = id

        self.asstes = asset.Assets()
        self.create_widgets()

    def create_widgets(self):
        self.book_scan_page_fm = tk.Frame(self, highlightbackground=self.asstes.bg_color, highlightthickness=2, bg='#FFFFFF')
        self.book_scan_page_fm.pack(pady=0)
        self.book_scan_page_fm.configure(width=890, height=780)

        self.title_frame = tk.Frame(self.book_scan_page_fm, bg=self.asstes.bg_color)
        self.title_frame.place(x=0, y=0)
        self.title_frame.configure(width=890, height=45)

        self.label1 = tk.Label(self.book_scan_page_fm, fg='#119F46', text='리더기에 책을 스캔하세요', font='arial 28 bold',
                               bg='#FFFFFF')
        self.label1.place(x=250, y=80)

        self.entry = tk.Entry(self.book_scan_page_fm, text='', highlightbackground=self.asstes.bg_color,
                              highlightthickness=2, font=('', 28))
        self.entry.place(x=270, y=160, width=380)
        self.entry.bind('<Return>', self.function_to_run)
        self.entry.focus()

        self.list_frame = tk.Frame(self.book_scan_page_fm, highlightbackground=self.asstes.bg_color,
                                   highlightthickness=2)
        self.list_frame.place(x=190, y=240)
        self.list_frame.configure(width=600, height=285)

        self.listbox = tk.Listbox(self.list_frame, font=('arial', 18),
                                  width=40, height=10, bg='#FFEDF1', fg='#2B2B2B', cursor='hand2',
                                  selectbackground='#5a95ff')

        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.bottom_frame = tk.Frame(self.book_scan_page_fm, bg='#F5EBDD')
        self.bottom_frame.place(x=0, y=565)
        self.bottom_frame.configure(width=885, height=210)

        self.borrow_btn = tk.Button(self.bottom_frame, text='대출 하기', font='arial 30 bold', bg='#4285F4', fg='white',
                                    bd=0)
        self.borrow_btn.place(x=230, y=50)

        self.forward_welcome_btn = tk.Button(self.bottom_frame, text='시작 화면', font='arial 30 bold', bg='#FE853E',
                                             fg='white', bd=0, command=self.forwad_to_welcome_page)
        self.forward_welcome_btn.place(x=470, y=50)



    def function_to_run(self, event):
        code = str(self.entry.get())
        print(code)

        if code=='9781234567897':
            data = '파이썬 프로그래밍 (00001) 홍길동'

        elif code == '978123456788':
            data = '자바 프로그래밍 (00002) 홍길동'

        self.listbox.insert(tk.END, data)
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def forwad_to_welcome_page(self):
        self.book_scan_page_fm.destroy()
        self.update()

        welcome_page_fm = welcomePage.WelcomePage(self)
        welcome_page_fm.pack()