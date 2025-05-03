import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")

current_player = "X"
buttons = []


def check_winner(): #могут быть 3 вида победы их все нужно записать и проверить (по горизонтали, по вертикали, по диагонали)
   for i  in range (3):
       if buttons [i][0]['text'] == buttons [i][1]['text'] == buttons [i][2]['text'] != "":
           return True
       if buttons [0][i]['text'] == buttons [1][i]['text'] == buttons [2][i]['text'] !="":
           return True

   if buttons [0][0]['text'] == buttons [1][1]['text'] == buttons [2][2]['text'] !="":
       return True
   if buttons [0][2]['text'] == buttons [1][1]['text'] == buttons [2][0]['text'] !="":
       return True

   return False


def on_click(row, col):
   global current_player

   if buttons [row][col]['text'] != "": #чтобы нельзя было повторно поставить какое-то значение
       return
   buttons[row][col]['text'] = current_player #значение будет поставляться в зависимости от того, очередь какого игрока сейчас

   if check_winner():
       messagebox.showinfo("Game is finished",f"player{current_player} is the winner!")

   current_player = "0" if current_player == "X" else "X" #смена игрока

for i in range(3):
   row = []
   for j in range(3):
       btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, command=lambda r=i, c=j: on_click(r, c))
       btn.grid(row=i, column=j)
       row.append(btn)
   buttons.append(row)


window.mainloop()
