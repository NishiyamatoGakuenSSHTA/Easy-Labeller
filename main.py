from doctest import master
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

from PIL import Image, ImageTk, ImageOps


class Application(tk.Frame):
    def __init__(self, master=None) -> None:
        super().__init__(master=master)
        self.pack()

        self.master.title("Easy Labeller")
        self.master.geometry("400x300")

        self._create_menu()

        self.back_color = "#008888"
        self.canvas = tk.Canvas(self.master, bg=self.back_color)
        self.canvas.pack(expand=True, fill=tk.BOTH)

    def _create_menu(self):
        menubar = tk.Menu(self)

        menu_file = tk.Menu(menubar, tearoff=False)
        menu_file.add_command(label="画像をファイルを開く", command=self._menu_file_open_click, accelerator="Ctrl+O")
        menu_file.add_separator()
        menu_file.add_command(label="終了", command=self.master.destroy)
        menu_file.bind_all("<Control-o>", self._menu_file_open_click)

        menubar.add_cascade(label="ファイル", menu=menu_file)

        self.master.config(menu=menubar)

    def _menu_file_open_click(self, event=None):
        filename = filedialog.askopenfilename(
            title="ファイルを開く",
            filetypes= [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ],
            initialdir="./"
        )
        self._disp_image(filename)

    def _disp_image(self, filename):
        if not filename:
            return

        pil_image = Image.open(filename)

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        pil_image = ImageOps.pad(pil_image, (canvas_width, canvas_height), color=self.back_color)

        self.photo_image = ImageTk.PhotoImage(image=pil_image)

        self.canvas.create_image(
            canvas_width / 2,
            canvas_height / 2,
            image=self.photo_image
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
