import tkinter as tk 
from tkinter import Canvas, PhotoImage 
from checkers.enums import SideType 
from checkers.constants import MENU_COLOR, CELL_SIZE, X_SIZE, Y_SIZE
from checkers.game import Game 

class CheckersApp:
    def __init__(self): 
        self.root = tk.Tk() 
        self.root.geometry("800x600") 
        self.root.title("Шашки") 
        self.root.iconphoto(False, PhotoImage(file='icon.png')) 
        self.root.configure(bg=MENU_COLOR)
        self.player_side = None

        self.play_image = tk.PhotoImage(file="play_button.png") 
        self.option_image = tk.PhotoImage(file="option_button.png") 
        self.exit_image = tk.PhotoImage(file="exit_button.png") 
        self.checkers_image = tk.PhotoImage(file="title_of_game.png") 
        self.black_side_image = tk.PhotoImage(file="side_black.png")
        self.white_side_image = tk.PhotoImage(file="side_white.png")

        self.frame = tk.Frame(self.root, bg=MENU_COLOR) 
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) 

        self.checkers_label = tk.Label(self.frame, image=self.checkers_image, bg=MENU_COLOR) 
        self.checkers_label.pack(pady=(40, 20)) 

        self.play_button = tk.Button(self.frame, image=self.play_image, command=self.choose_color_button, borderwidth=0, bg=MENU_COLOR, activebackground=MENU_COLOR) 
        self.play_button.pack(pady=10) 

        self.option_button = tk.Button(self.frame, image=self.option_image, command=self.move_to_option, borderwidth=0, bg=MENU_COLOR, activebackground=MENU_COLOR) 
        self.option_button.pack(pady=10) 

        self.exit_button = tk.Button(self.frame, image=self.exit_image, command=self.exit_game, borderwidth=0, bg=MENU_COLOR, activebackground=MENU_COLOR) 
        self.exit_button.pack(pady=10) 

        self.main_canvas = None 
        self.game = None 
        self.restart_button = None 
        self.go_back_to_menu_button = None
        self.replace_side_button = None
        self.black_button=None
        self.white_button=None

    def start_game(self): 
        # Очищаем холст и создаем новый экземпляр игры 
        self.clear_canvas() 
        self.main_canvas = Canvas(width=CELL_SIZE * (X_SIZE), height=CELL_SIZE * (Y_SIZE)) 
        self.main_canvas.pack(expand=True) 
        self.game = Game(self.main_canvas, X_SIZE, Y_SIZE, self.player_side) 

        # Добавляем кнопку "Начать заново" 
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game) 
        self.restart_button.place(relx=0.06, rely=0.45, anchor=tk.CENTER) 

        # Добавляем кнопку "Выход в меню" 
        self.go_back_to_menu_button = tk.Button(self.root, text="Menu", command=self.go_back_to_menu) 
        self.go_back_to_menu_button.place(relx=0.06, rely=0.5, anchor=tk.CENTER) 

        self.replace_side_button = tk.Button(self.root, text="Replace side", command=self.choose_color_button) 
        self.replace_side_button.place(relx=0.06, rely=0.55, anchor=tk.CENTER) 

        self.main_canvas.bind("<Motion>", self.game.mouse_move) 
        self.main_canvas.bind("<Button-1>", self.game.mouse_down) 
    
    def choose_color_button(self): 
        self.clear_canvas() 
        self.main_canvas = Canvas(width=CELL_SIZE * X_SIZE, height=CELL_SIZE * Y_SIZE, bg=MENU_COLOR) 
        self.main_canvas.pack(expand=True) 

        self.white_button = tk.Button(self.root, image=self.white_side_image, command=self.select_color_game_white, borderwidth=0, bg=MENU_COLOR, activebackground=MENU_COLOR)
        self.white_button.place(relx=0.35, rely=0.45, anchor=tk.CENTER) 

        self.black_button = tk.Button(self.root, image=self.black_side_image, command=self.select_color_game_black, borderwidth=0, bg=MENU_COLOR, activebackground=MENU_COLOR)
        self.black_button.place(relx=0.65, rely=0.45, anchor=tk.CENTER)


    def select_color_game_white(self):
        self.player_side = SideType.WHITE
        self.black_button.destroy()
        self.white_button.destroy()
        self.start_game()
        
    def select_color_game_black(self):
        self.player_side = SideType.BLACK
        self.black_button.destroy()
        self.white_button.destroy()
        self.start_game()


    def move_to_option(self): 
        print("Оно работает") 

    def exit_game(self): 
        self.root.destroy() 

    def clear_canvas(self): 
        # Очищаем холст от предыдущих объектов 
        if self.main_canvas: 
            self.main_canvas.destroy() 
        if self.restart_button: 
            self.restart_button.destroy() 
        if self.go_back_to_menu_button: 
            self.go_back_to_menu_button.destroy() 
        if self.replace_side_button:
            self.replace_side_button.destroy()

    def restart_game(self): 
        self.start_game() 

    def go_back_to_menu(self): 
        self.clear_canvas() 

app = CheckersApp() 
app.root.mainloop()

