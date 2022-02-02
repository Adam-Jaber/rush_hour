from tkinter import messagebox
import game_exceptions
from playsound import playsound
CAR_COLOR_DICT = {'red': 2, 'purple': 3, 'yellow': 3, 'green': 2, 'blue': 2}
DIRECTION_DICT = {'Left': 0, 'Down': 1, 'Right': 2, 'Up': 3}


def try_wrapper(fun):
    def dec_fun(*args, **kwargs):
        try:
            fun(*args, **kwargs)
        except AssertionError:
            messagebox.showerror("error", "the car doesnt move in that direction")
        except game_exceptions.RushHourException as e:
            messagebox.showerror("error", e)
    return dec_fun


class Car:
    def __init__(self, master, color, position, rotation):
        self.rotation = rotation
        self.master = master
        self.position = position
        self.color = color
        self.squares_to_paint = list()

        self._pack_car()
        self._enable_movement()

    def _pack_car(self):
        row, column = self.position

        for i in range(CAR_COLOR_DICT[self.color]):
            if self.rotation:
                self.squares_to_paint.append((row + i, column))
            else:
                self.squares_to_paint.append((row, column + i))

        self.paint_squares(self.squares_to_paint)

    @try_wrapper
    def move_car(self, event):
        assert DIRECTION_DICT[event.keysym] % 2 == self.rotation

        direction_to_tuple = {'Right': (0, 1), 'Left': (0, -1), 'Up': (-1, 0), 'Down': (1, 0)}
        add_to_row, add_to_column = direction_to_tuple[event.keysym]
        new_positions = [(row + add_to_row, column + add_to_column) for (row, column) in self.squares_to_paint]

        if not self.check_positions(new_positions):
            raise game_exceptions.BorderException

        if self.check_collision(new_positions):
            playsound("yt5s (mp3cut.net).mp3")
            raise game_exceptions.CollisionException

        del_position = [pos for pos in self.squares_to_paint if pos not in new_positions][0]

        self.squares_to_paint = new_positions
        self.paint_squares(self.squares_to_paint, del_position)

        new_focus = (self.master.focus_get().row + add_to_row, self.master.focus_get().column + add_to_column)
        self.master.square_dict[new_focus].focus_set("car moved")

        self._clear_movement()
        self._enable_movement()

    def paint_squares(self, squares_to_paint, square_to_delete=None):
        for square in squares_to_paint:
            self.master.square_dict[square].paint(self.color)

        if square_to_delete is not None:
            self.master.square_dict[square_to_delete].unpaint()

    def _enable_movement(self):
        self.frame_list = []
        for position in self.squares_to_paint:
            self.frame_list.append(self.master.square_dict[position])
        for square in self.frame_list:
            square.bind("<Up>", self.move_car)
            square.bind("<Down>", self.move_car)
            square.bind("<Right>", self.move_car)
            square.bind("<Left>", self.move_car)

    def _clear_movement(self):
        for square in self.frame_list:
            square.unbind("<Up>")
            square.unbind("<Down>")
            square.unbind("<Left>")
            square.unbind("<Right>")

    @staticmethod
    def check_positions(position_list):
        for row, column in position_list:
            if 0 <= row <= 5 and 0 <= column <= 5:
                pass
            else:
                return False
        return True

    def check_collision(self, new_positions):
        for position in new_positions:
            if self.master.square_dict[position].color not in ['white', self.color]:
                return True
        return False
