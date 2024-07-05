import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import cv2
import assets as asset
import welcomePage


class ReturnPage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.asstes = asset.Assets()
        self.create_widgets()

    def create_widgets(self):
        self.return_page_fm = tk.Frame(self, highlightbackground=self.asstes.bg_color, highlightthickness=2, bg='#FFFFFF')
        self.return_page_fm.pack(pady=0)
        self.return_page_fm.configure(width=890, height=780)