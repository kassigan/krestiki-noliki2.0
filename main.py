import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")

current_player = "X"
buttons = []

# Счётчики
score_x = 0
score_o = 0

# Метка для счёта
score_label = tk.Label(window, text="Счёт — X: 0 | O: 0", font=("Arial", 14))
score_label.grid(row=0, column=0, columnspan=3, pady=10)

def update_score():
    score_label.config(text=f"Счёт — X: {score_x} | O: {score_o}")


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
   global current_player,  score_x, score_o

   if buttons [row][col]['text'] != "": #чтобы нельзя было повторно поставить какое-то значение
       return
   buttons[row][col]['text'] = current_player #значение будет поставляться в зависимости от того, очередь какого игрока сейчас

   if check_winner():
       if current_player == "X":
           score_x += 1
       else:
           score_o += 1

       update_score()
       messagebox.showinfo("Game Over!",f"player{current_player} is the winner!")
       disable_buttons()
       return


# Смена игрока
   current_player = "0" if current_player == "X" else "X"


def disable_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")

def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn.config(text="", state="normal")



# Создание кнопок для игрового поля
for i in range(3):
   row = []
   for j in range(3):
       btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2,
                        highlightbackground="#33ddff",
                       command=lambda r=i, c=j: on_click(r, c))
       btn.grid(row=i + 1, column=j)  # +1, потому что счёт на первой строке
       row.append(btn)
   buttons.append(row)

# Кнопка сброса игры (не сбрасывает счёт)
reset_button = tk.Button(window, text="Сброс", highlightbackground="#d133ff", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3,  sticky="nsew",pady=15)

window.mainloop()
