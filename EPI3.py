import tkinter as tk
root = tk.Tk()
from tkinter import messagebox
import requests
root.title("Conversor de Moedas")
limon_grey = "#d7ded8"
root.geometry("380x550+0+0")
root.wm_resizable(height=True,width=True)
root.configure(bg=limon_grey)
lt1 = tk.Label(root, text="Conversor de Moedas",font="20",bg=yellow)
lt1.place(width=380, height=50,x=1,y=1)

root.mainloop()
