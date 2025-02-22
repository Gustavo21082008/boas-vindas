import tkinter as tk
root = tk.Tk()
#variável
root.title("Color Changer")
roxo = "#d657d0"
verde = "#57d65d"
amarelo = "#ccd621"
azul = "#6457d0"
root.geometry("500x300+200+200")
root.wm_resizable(height=True,width=True)
root.configure(background=roxo)

def Fundo1():
    root.configure(bg=azul)


lt1 =tk.Label(root, text="azul",font="Times 15 bold italic")
bt1 = tk.Button(root,text='azul',command=Fundo1,fg=azul)
bt1.place(width=200, height=125,x=1,y=1)


def Fundo2():
    root.configure(bg=roxo)

lt2 =tk.Label(root, text="Roxo",font="Times 15 bold italic")
bt2 = tk.Button(root,text='Roxo',command=Fundo2,fg=roxo)
bt2.place(width=200, height=125,x=1,y=185)


def Fundo3():
    root.configure(bg=verde)

lt3 =tk.Label(root, text="verde",font="Times 15 bold italic")
bt3 = tk.Button(root,text='verde',command=Fundo3,fg=verde)
bt3.place(width=200, height=125,x=300,y=185)


def Fundo4():
    root.configure(bg=amarelo)

lt1 =tk.Label(root, text="amarelo",font="Times 15 bold italic")
bt1 = tk.Button(root,text='amarelo',command=Fundo4)
bt1.place(width=200, height=125,x=300,y=1)

root.mainloop()