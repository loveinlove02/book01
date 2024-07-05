import tkinter as tk
import welcomePage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('도서관리 시스템')
        self.geometry('900x800')
        self.resizable(False, False)

        self.create_widgets()


    def create_widgets(self):
        welcome_page_frame = welcomePage.WelcomePage(self)
        welcome_page_frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()