import tkinter as tk
import psycopg2 as pg
from car import Car
from square import Square

LEVELS_DATA_COLUMNS = ['level_id', 'level_num', 'red', 'purple', 'pink', 'yellow',
                       'orange', 'light_green', 'green', 'blue', 'light_blue', 'black', 'grey']


class Board(tk.Frame):
    def __init__(self, master, level, user_id):
        super().__init__(master, width=420, height=420)

        self.square_dict = dict()
        self.level = level
        self.user_id = user_id

        for row in range(6):
            for column in range(6):
                self.square_dict[(row, column)] = Square(self, row, column)

        self.pack_squares()
        self.set_level()

    def set_level(self):
        self._clear_board()

        self.cars_dict = dict()

        con = pg.connect(database='rush_hour', user='postgres', password='jaber2213')
        self.cur = con.cursor()
        self.cur.execute(f'SELECT * FROM levels WHERE level_num = {self.level}')
        level_info = self.cur.fetchone()
        self.level_id = level_info[0]

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
            self.square_dict[(row_, column_)].grid(row=row_, column=column_)

    def check_win(self):
        if self.square_dict[(2, 5)].color == 'red':
            self.cur.execute(f"""INSERT INTO user_level_passed
                                VALUES(
                                {self.user_id},
                                {self.level_id}
                                )""")
            self.cur.commit()
            self.master.wining_screen(self.user_id, self)
