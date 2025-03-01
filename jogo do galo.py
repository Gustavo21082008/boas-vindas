import tkinter as tk
def clica_botao(index):
 global Jogador_Atual, board,buttons

 if board[index] == "":
  board[index] = Jogador_Atual
  buttons[index].config(text=Jogador_Atual)
   Jogador_Atual = "O" if Jogador_Atual == "X" else "X"

root = tk.Tk()
# variável
root.title("Jogo do Velha")
Jogador_Atual = "X" #define o jogador inicial com "X"
board = [""] * 9
buttons = []

for i in range(9):
   button = tk.Button(root, text='',font=('normal',40),width=5, height=2,command=lambda i=i: clica_botao(i))
   button.grid(row=i//3, column=i%3)
   buttons.append(button)


root.mainloop()