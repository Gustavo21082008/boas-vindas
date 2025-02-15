import tkinter as tk


root = tk.Tk()
#variável
root.title("SharkCoders")

def teste():
    print("olá Shark coders")

root.geometry("500x300+200+200")


button1 = tk.Button(root, text="Click Me",font="Times 20 bold italic",command=teste())
button1.pack(pady=10)
def teste2():
    print("i am good thank you!")

button2 = tk.Button(root, text="how are you?",command=teste2())
button2.pack(pady=20)

def Button3():
    print("")

button3 = tk.Button(root, text="")
button3.pack(pady=30)
lh1 = tk.Label(root,text="Hello")
lh1.pack(pady=25)
root.wm_resizable(height=True,width=True)

root.mainloop()