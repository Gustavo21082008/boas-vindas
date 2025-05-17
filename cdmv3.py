import tkinter as tk
from tkinter import ttk
import requests

moeda = ["EUR","USD","BRL"]

branco = "#ffffff"
azul = "#3a6efc"
vermelho = "#f00a11"
preto = "#000000"

tela = tk.Tk()
tela.geometry("650x600+0+0")

label_de = tk.Label(tela, text="De:", font=("Arial", 14), fg=preto,anchor='w')
label_de.place(width=100, height=60,x=15,y=320)
moeda_de = ttk.Combobox(tela, text="De",font='time 11 bold', justify="center")
moeda_de.place(width=150,height=35, x=16,y=360)
moeda_de['values']= (list)
def converter():
 de = moeda.get()
 para = moeda_para.get()
 cotacao = requests.get('https://economia.awesomeapi.com.br/last/{}'.format(de,"-",para))
 cotacao = cotacao.json()
 cotacao_moeda = float(cotacao['{}'.format(de+para)]["bid"])

valor= float(valor_input.get())
r = round(cotacao * valor, 2)

button = tk.Button(tela, text="converter", command='Converter', font="time 11 bold",bg=azul,fg=branco)
button.place(width=100,height=36,x=300,y=360)
label_para = tk.Label(tela, text="Para",font="Arial 14",fg=preto,anchor="w")
label_para.place(width=100,height=60,x=300,y=320)
moeda_para = ttk.Combobox(tela, text="Para",font="time 11 bold",justify="center")
moeda_para.place(width=150,height=36,x=300,y=360)
moeda_para['values']= (list)

valor = tk.Entry(tela,font="Time 11 bold",justify="center")
valor.place(width=150,height=35,x=300,y=400)



tela.mainloop()