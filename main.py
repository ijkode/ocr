# Ocr
# author: Liran Libster

import pytesseract as tess
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.font as font

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

root = tk.ThemedTk()
root.get_themes()
root.set_theme("arc")
root.title('Ocr')
root.iconbitmap(r'eyescan.ico')
root.geometry("500x370")
myFont = font.Font(family='Tahoma')
image = Image.open("background.png")
image = ImageTk.PhotoImage(image)
bg_label = ttk.Label(root, image=image)
bg_label.place(x=0, y=0)
bg_label.image = image
photo = None
file = None
pop = None


def open_img():
    global photo
    global pop
    global file
    my_text.delete(1.0, END)
    filename = filedialog.askopenfilename()
    photo = ImageTk.PhotoImage(file=filename)
    file = filename
    if pop is not None:
        pop.destroy()
    pop = Toplevel(root)
    pop.title("Ocr")
    pop.iconbitmap(r"eyescan.ico")
    width = photo.width() + 100
    height = photo.height() + 100
    size = str(width) + "x" + str(height)
    pop.geometry(size)

    extract_text()
    pop_lable = Label(pop)
    pop_lable.pack(pady=10)

    my_frame = Frame(pop)
    my_frame.pack(pady=5)

    pic = Label(my_frame, image=photo, borderwidth=0)
    pic.grid(row=0, column=0, padx=10)


def extract_text():
    lang = ""
    if clicked.get() == "English":
        lang = 'eng'
    if clicked.get() == "Hebrew":
        lang = 'heb'
    text = tess.image_to_string(file, lang)
    text = text[:-1]
    my_text.insert(END, text)


def cut_text():
    my_text.event_generate("<<Cut>>")


def copy_text():
    my_text.event_generate("<<Copy>>")


def paste_text():
    my_text.event_generate("<<Paste>>")


def context_menu(event):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()


my_text = Text(root, width=35, height=10, font=("Tahoma", 16))
my_text.pack(pady=5)
clicked = StringVar()
clicked.set("English")
drop = ttk.OptionMenu(root, clicked, "English", "Hebrew", "English")
drop.pack()
open_button = ttk.Button(root, text="Open Photo", command=open_img)
open_button.pack(pady=5)
menu = Menu(root, tearoff=0)
menu.add_command(label="Cut", command=cut_text)
menu.add_command(label="Copy", command=copy_text)
menu.add_command(label="Paste", command=paste_text)
menu.add_separator()
menu.add_command(label="Exit", command=root.destroy)

root.bind("<Button-3>", context_menu)
root.mainloop()
