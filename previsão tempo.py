import requests

import tkinter as tk
root = tk.Tk()
root.title("Informações Metereológicas")
root.geometry("500x300+0+0")
white = "#ffffff"
yellow = "#fff703"
grey = "#c7c1c1"

root.wm_resizable(height=True,width=True)
root.configure(bg=white)
lt1 = tk.Label(text="Informações metereológicas",font="20",bg=yellow)
lt1.place(width=500,height=50,x=1,y=1)
lt2 = tk.Label(root,text="Cidade:",font=15,bg=white)
lt2.place(width=60,height= 20,x=10,y=70)
entry_city = tk.Entry(root, font=15)
entry_city.place(width=200, height=25,x=80,y=70)
def obter_dados_meteorológicos():
    city = entry_city.get()
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=136af85a067876d79bf7b40102faf65b&units=metric".format(city)
    res = requests.get(url)
data = res.json()

temp = data ["main"] ["temp"]
humid = data ["main"] ["humidity"]
wind = data ["wind"] ["speed"]
desc = data ["weather"] [0] ["description"]

print("Description" + desc)
print("Temp: {}ºC".format(temp))
print("Wind speed: {}m/s".format(wind))
print("Humidity: {}%".format(humid))



root.mainloop()
#projecto Final