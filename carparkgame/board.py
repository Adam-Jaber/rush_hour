import tkinter as tk
import requests
from car import Car
from square import Square

LEVELS_DATA_COLUMNS = ['level_id', 'level_num', 'red', 'purple', 'pink', 'yellow',
                       'orange', 'green', 'blue', 'black', 'grey', 'cyan', 'magenta']


class Board(tk.Frame):
    def __init__(self, master, level, user_id):
        super().__init__(master, width=420, height=420)

        self.square_dict = dict()
        self.level = level
        self.user_id = user_id
        self.cars_dict = dict()

        for row in range(6):
            for column in range(6):
                self.square_dict[(row, column)] = Square(self, row, column)

        self.pack_squares()
        self.set_level()

    def set_level(self):
        self._clear_board()

        level_info_dict = requests.get(f"https://2rc2iohsvl.execute-api.us-east-2.amazonaws.com/test/level_info?level_num={self.level}").json()
        self.level_id = level_info_dict['level_id']

        for color in level_info_dict:
            if isinstance(level_info_dict[color], str):
                x, y, r = map(int, level_info_dict[color].split(' '))
                self.cars_dict[color] = Car(self, color, (x, y), r)

    def _clear_board(self):
        for square in self.square_dict:
            self.square_dict[square].unpaint()

    def pack_squares(self):
        for (row_, column_) in self.square_dict:
            self.square_dict[(row_, column_)].grid(row=row_, column=column_)

    def check_win(self):
        if self.square_dict[(2, 5)].color == 'red':
            passed_levels_list = requests.get(f"https://2rc2iohsvl.execute-api.us-east-2.amazonaws.com/test/passed_levels?user_id={self.user_id}").json()

            if self.level not in passed_levels_list:
                requests.post(f"https://2rc2iohsvl.execute-api.us-east-2.amazonaws.com/test/passed_levels?user_id={self.user_id}&level_id={self.level_id}")

            self.master.winning_screen(self.user_id, self)
