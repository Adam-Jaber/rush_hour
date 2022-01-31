import tkinter as tk
import psycopg2 as pg
from car import Car
from square import Square

LEVELS_DATA_COLUMNS = ['level_id', 'level_num', 'red', 'purple', 'pink', 'yellow', 'orange', 'light_green', 'green', 'blue', 'light_blue', 'black', 'grey']


class Board(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=420, height=420)

        self.square_dict = dict()
        for row in range(6):
            for column in range(6):
                self.square_dict[(row,column)] = Square(self, row, column)

        self.pack_squares()

    def set_level(self, level):
        self._clear_board()

        self.cars_dict = dict()

        con = pg.connect(database='rush_hour', user='postgres', password='******')
        cur = con.cursor()
        cur.execute(f'SELECT * FROM LEVELS WHERE level_num = {level}')
        level_info = cur.fetchone()

        for car in level_info:
            if isinstance(car, str):
                color = LEVELS_DATA_COLUMNS[level_info.index(car)]
                x, y, r = map(int, car.split(' '))
                self.cars_dict[color] = Car(self, color, (x, y), r)

    def _clear_board(self):
        for square in self.square_dict:
            self.square_dict[square].unpaint()

    def pack_squares(self):
        for (row_, column_) in self.square_dict:
            self.square_dict[(row_,column_)].grid(row=row_, column=column_)
            #print('packed frame')

