import requests
from tkinter import *
from tkinter import messagebox


def get_weather():
    city = entry_city.get().strip()
    if not city:
        messagebox.showwarning("Aviso","Por favor insira o Nome da cidade.")
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid=136af85a067876d79bf7b40102faf65b&units=metric"
    )
    try:
        res = requests.get(url)
        data = res.json()
        if res.status_code != 200 or "main" not in data:
            raise ValueError(data.get("message", "Erro desconhecido."))
        temp = data["main"]["temp"]
        humid = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        desc = data["weather"][0]["description"]

        result_text = (f"Descrição:{desc}\n"
                       f"Temperatura:{temp}ºC\n"
                       f"Velocidade do vento:{wind}m/s\n"
                       f"Umidade: {humid}%"
                    )
        result_label.config(text=result_text)
    except Exception as e:
        result_label.config(text="")
        messagebox.showerror("erro",f"não foi possível obter as informações: {e}")


root = Tk()
root.title("Informações Meteorológicas")
root.geometry("500x300+0+0")
white = "#ffffff"
yellow = "#fff703"

root.resizable(height=True, width=True)
root.configure(bg=white)

lt1 = Label(root, text="Informações meteorológicas", font=("Arial", 20), bg=yellow)
lt1.place(width=500, height=50, x=1, y=1)
lt2 = Label(root, text="Cidade:", font=("Arial", 15), bg=white)
lt2.place(width=60, height=20, x=10, y=70)
entry_city = Entry(root, font=("Arial", 15))
entry_city.place(width=200, height=25, x=80, y=70)
bt1 = Button(root, text="Pesquisar", command=get_weather)
bt1.place(width=100, height=30, x=300, y=65)

result_label = Label(root, text="", font=("Arial", 14), bg=white, justify="left", anchor="nw")
result_label.place(width=480, height=150, x=10, y=110)

root.mainloop()
#projecto Final