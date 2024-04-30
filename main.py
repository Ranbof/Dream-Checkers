import tkinter as tk
from tkinter import Canvas, PhotoImage
from checkers.game import Game
from checkers.constants import X_SIZE, Y_SIZE, CELL_SIZE, MENU_COLOR
def main_game_function():

    # Создание холста
    main_canvas = Canvas(width = CELL_SIZE * X_SIZE, height = CELL_SIZE * Y_SIZE)
    main_canvas.pack()

    game = Game(main_canvas, X_SIZE, Y_SIZE)
    

    main_canvas.bind("<Motion>", game.mouse_move)
    main_canvas.bind("<Button-1>", game.mouse_down)



def start_game():
    main_game_function()

def move_to_option():
    print("Оно работает")

def exit_game():
    root.destroy()

root = tk.Tk()
root.geometry("800x600")
root.title("Шашки")
root.iconphoto(False, PhotoImage(file = 'icon.png'))

# Устанавливаем цвет фона
root.configure(bg = MENU_COLOR)

play_image = tk.PhotoImage(file = "play_button.png")
option_image = tk.PhotoImage(file = "option_button.png")
exit_image = tk.PhotoImage(file = "exit_button.png")
checkers_image = tk.PhotoImage(file = "title_of_game.png")

#Размещение элементов
frame = tk.Frame(root, bg = MENU_COLOR)
frame.place(relx = 0.51, rely = 0.4, anchor = tk.CENTER)

# Размещение слово 'Chekers'
checkers_label = tk.Label(frame, image = checkers_image, bg = MENU_COLOR)
checkers_label.pack(pady = (40, 20))

# Кнопки с изображениями и прозрачным фоном
play_button = tk.Button(frame, image=play_image, command = start_game, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
play_button.pack(pady = 10)

option_button = tk.Button(frame, image = option_image, command = move_to_option, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
option_button.pack(pady = 10)

exit_button = tk.Button(frame, image = exit_image, command = exit_game, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
exit_button.pack(pady = 10)

root.mainloop()

