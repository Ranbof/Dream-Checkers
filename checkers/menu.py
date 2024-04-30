from tkinter import Canvas

from checkers.constants import *


class Menu:
    def __init__(self, canvas: Canvas, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__canvas = canvas
        self.__draw_menu()

    def __draw_menu(self):
        '''Отрисовка меню'''
        self.__canvas.delete('all')
        for y in range(self.__width):
            for x in range(self.__height):
                self.__canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, x * CELL_SIZE + CELL_SIZE, y * CELL_SIZE + CELL_SIZE, fill = MENU_COLOR, width = 0, tag = 'boards')
                self.__canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, x * CELL_SIZE + CELL_SIZE, y * CELL_SIZE + CELL_SIZE, fill = MENU_COLOR, width = 0, tag = 'boards')
        self.make_button("Играть", (X_SIZE * CELL_SIZE) / 2.35, (Y_SIZE * CELL_SIZE) / 3, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.make_button("Настройки", (X_SIZE * CELL_SIZE) / 2.35, (Y_SIZE * CELL_SIZE) / 2.4, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.make_button("Выход", (X_SIZE * CELL_SIZE) / 2.35, (Y_SIZE * CELL_SIZE) / 2, BUTTON_WIDTH, BUTTON_HEIGHT)

    def make_button(self, text, x, y, width, height):
        '''Создание кнопки'''
        self.__canvas.create_rectangle(x, y, x + width, y + height, fill = HOVER_BORDER_COLOR, width = 0, tag = 'buttons')
        self.__canvas.create_text(x + width // 2, y + height // 2, text = text, font = ('Arial', 12), fill = 'white', tag = 'buttons')


    
    