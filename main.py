import tkinter as tk
from tkinter import ttk, Canvas, PhotoImage
from checkers.enums import SideType
from checkers.constants import MENU_COLOR, CELL_SIZE, X_SIZE, Y_SIZE
from checkers.game import Game
import pygame

class CheckersApp:
    def __init__(self): 
        pygame.mixer.init()
        self.root = tk.Tk() 
        self.root.geometry("800x600") 
        self.root.title("Шашки") 
        self.root.iconphoto(False, PhotoImage(file = 'icon.png')) 
        self.root.configure(bg = MENU_COLOR)

        self.player_side = None
        self.other_player_side = None


        self.num_move_prediction = 4 # Количество ходов для предсказания:
        # Легкий уровень сложности для начинающих (Максимум: 2)
        # Для комфортной игры (Максимум: 4)
        # Для большой сложности (Максимум: 6)


        self.user_vs_user_mode = False

        self.play_image = tk.PhotoImage(file = "play_button.png") 
        self.option_image = tk.PhotoImage(file = "option_button.png") 
        self.exit_image = tk.PhotoImage(file = "exit_button.png") 
        self.checkers_image = tk.PhotoImage(file = "title_of_game.png") 
        self.black_side_image = tk.PhotoImage(file = "side_black.png")
        self.white_side_image = tk.PhotoImage(file = "side_white.png")
        self.settings_image = tk.PhotoImage(file = "settings.png")

        self.main_canvas = None 
        self.game = None

        self.restart_button = None 
        self.go_back_to_menu_button = None
        self.replace_side_button = None
        self.black_button = None
        self.white_button = None
        self.settings_button = None
        self.close_settings_button = None
        self.mode_button = None
        self.music_button = None

        self.difficulty_label = None
        self.difficulty_entry = None

        self.playlist_label = None
        self.playlist_combobox = None
        self.music_on = False
        self.music_playlist = ["background_music1.wav", "background_music2.wav", "background_music3.wav"]
        self.selected_music = tk.StringVar(value=self.music_playlist[0])

        self.frame = None
        self.show_main_menu()

    def start_game(self): 
        self.clear_canvas() 
        self.main_canvas = Canvas(self.root, width = CELL_SIZE * X_SIZE, height = CELL_SIZE * Y_SIZE) 
        self.main_canvas.pack(expand = True)
        
        if self.user_vs_user_mode:
            self.game = Game(self.main_canvas, X_SIZE, Y_SIZE, self.player_side, self.other_player_side, self.num_move_prediction)
        else:
            self.game = Game(self.main_canvas, X_SIZE, Y_SIZE, self.player_side, None, self.num_move_prediction)

        self.restart_button = tk.Button(self.root, text = "Restart", command = self.restart_game) 
        self.restart_button.place(relx = 0.06, rely = 0.45, anchor = tk.CENTER) 

        self.go_back_to_menu_button = tk.Button(self.root, text = "Menu", command = self.go_back_to_menu) 
        self.go_back_to_menu_button.place(relx = 0.06, rely = 0.5, anchor = tk.CENTER) 

        self.replace_side_button = tk.Button(self.root, text = "Replace side", command = self.choose_color_button) 
        self.replace_side_button.place(relx = 0.06, rely = 0.55, anchor = tk.CENTER) 

        self.main_canvas.bind("<Motion>", self.game.mouse_move) 
        self.main_canvas.bind("<Button-1>", self.game.mouse_down) 

    def choose_mode(self):
        self.clear_canvas()
        self.clear_frame()

        self.frame = tk.Frame(self.root, bg = MENU_COLOR)
        self.frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

        mode_label = tk.Label(self.frame, text = "Choose mode:", font = ("Arial", 16), bg = MENU_COLOR)
        mode_label.grid(row = 0, column = 0, columnspan = 2, pady = (20, 10))

        player_vs_player_button = tk.Button(self.frame, text = "Player vs. Player", command = self.start_player_vs_player, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
        player_vs_player_button.grid(row = 1, column = 0, columnspan = 2, pady = (10, 10))

        player_vs_ai_button = tk.Button(self.frame, text = "Player vs. AI", command = self.start_player_vs_ai, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
        player_vs_ai_button.grid(row = 2, column = 0, columnspan = 2, pady = (10, 20))

    def choose_color_button(self): 
        self.clear_canvas()
        self.clear_frame()

        self.main_canvas = Canvas(self.root, width = CELL_SIZE * X_SIZE, height = CELL_SIZE * Y_SIZE, bg = MENU_COLOR) 
        self.main_canvas.pack(expand = True) 

        self.white_button = tk.Button(self.root, image = self.white_side_image, command = self.select_color_game_white, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
        self.white_button.place(relx = 0.35, rely = 0.45, anchor = tk.CENTER) 

        self.black_button = tk.Button(self.root, image = self.black_side_image, command = self.select_color_game_black, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
        self.black_button.place(relx = 0.65, rely = 0.45, anchor = tk.CENTER)

    def select_color_game_white(self):
        if self.user_vs_user_mode:
            self.player_side = SideType.WHITE
            self.other_player_side = SideType.BLACK
        else:
            self.player_side = SideType.WHITE
            self.other_player_side = None
        self.clear_color_buttons()
        self.start_game()
        
    def select_color_game_black(self):
        if self.user_vs_user_mode:
            self.player_side = SideType.BLACK
            self.other_player_side = SideType.WHITE
        else:
            self.player_side = SideType.BLACK
            self.other_player_side = None
        self.clear_color_buttons()
        self.start_game()

    def start_player_vs_player(self):
        self.user_vs_user_mode = True
        self.choose_color_button()

    def start_player_vs_ai(self):
        self.user_vs_user_mode = False
        self.choose_color_button()
    
    def move_to_option(self):
        self.clear_canvas()
        self.clear_frame()

        self.settings_button = tk.Label(self.root, image = self.settings_image, bg = MENU_COLOR)
        self.settings_button.pack(pady = (20,10))
        
        self.close_settings_button = tk.Button(self.root, text = "X", command = self.close_settings, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
        self.close_settings_button.place(relx = 0.95, rely = 0.05, anchor = tk.CENTER)

        self.music_button = tk.Button(self.root, text = "Музыка: Вкл" if self.music_on else "Музыка: Выкл", command = self.toggle_music, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
        self.music_button.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)

        self.difficulty_label = tk.Label(self.root, text = "Сложность:", bg = MENU_COLOR)
        self.difficulty_label.place(relx = 0.4, rely = 0.5, anchor = tk.CENTER)

        self.difficulty_entry = tk.Entry(self.root)
        self.difficulty_entry.place(relx = 0.6, rely = 0.5, anchor = tk.CENTER)

        self.playlist_label = tk.Label(self.root, text = "Выберите музыку:", bg = MENU_COLOR)
        self.playlist_label.place(relx = 0.4, rely = 0.6, anchor = tk.CENTER)

        self.playlist_combobox = ttk.Combobox(self.root, values = self.music_playlist, textvariable = self.selected_music)
        self.playlist_combobox.place(relx = 0.6, rely = 0.6, anchor = tk.CENTER)
        self.playlist_combobox.bind("<<ComboboxSelected>>", self.change_music)

    def close_settings(self):
        widgets = [
            self.settings_button,
            self.close_settings_button,
            self.music_button,
            self.difficulty_label,
            self.difficulty_entry,
            self.playlist_label,
            self.playlist_combobox,
        ]

        for widget in widgets:
            if widget:
                widget.destroy()
        self.show_main_menu()

    def toggle_music(self):
        self.music_on = not self.music_on
        if self.music_on:
            self.play_music(self.selected_music.get())
            self.music_button.config(text = "Музыка: Вкл")
        else:
            pygame.mixer.music.stop()
            self.music_button.config(text = "Музыка: Выкл")

    def play_music(self, track):
        pygame.mixer.music.load(track)
        pygame.mixer.music.play(-1)  

    def change_music(self, event):
        if self.music_on:
            self.play_music(self.selected_music.get())

    def show_main_menu(self):
        self.clear_canvas()
        self.clear_frame()

        self.frame = tk.Frame(self.root, bg = MENU_COLOR)
        self.frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

        self.checkers_label = tk.Label(self.frame, image=self.checkers_image, bg = MENU_COLOR)
        self.checkers_label.grid(row = 0, column = 0, pady = (40, 20))

        self.play_button = tk.Button(self.frame, image = self.play_image, command = self.choose_mode, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
        self.play_button.grid(row = 1, column = 0, pady = 10)

        self.option_button = tk.Button(self.frame, image = self.option_image, command = self.move_to_option, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
        self.option_button.grid(row = 2, column = 0, pady = 10)

        self.exit_button = tk.Button(self.frame, image = self.exit_image, command = self.exit_game, borderwidth = 0, bg = MENU_COLOR, activebackground = MENU_COLOR)
        self.exit_button.grid(row = 3, column = 0, pady = 10)

    def clear_canvas(self): 
        widgets = [
            self.main_canvas,
            self.restart_button,
            self.go_back_to_menu_button,
            self.replace_side_button, 
            self.settings_button,
            self.close_settings_button,
            self.black_button,
            self.white_button,
            self.music_button,
            self.difficulty_label,
            self.difficulty_entry,
            self.playlist_label,
            self.playlist_combobox,
        ]

        for widget in widgets:
            if widget:
                widget.destroy()

    def clear_frame(self):
        if self.frame and self.frame.winfo_exists():
            for widget in self.frame.winfo_children():
                widget.destroy()
            self.frame.destroy()

    def clear_color_buttons(self):
        if self.black_button:
            self.black_button.destroy() 
        if self.white_button:
            self.white_button.destroy()

    def restart_game(self): 
        self.start_game() 

    def go_back_to_menu(self): 
        self.show_main_menu()

    def exit_game(self): 
        self.root.destroy() 

app = CheckersApp() 
app.root.mainloop()