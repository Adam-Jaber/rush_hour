import tkinter as tk
from board import Board


def _enable_movement():
    for car in a.cars_dict.values():
        frame_list = []
        for position in car.squares_to_paint:
            frame_list.append(a.square_dict[position])
        for square in frame_list:
            square.bind("<Up>", car.move_car)
            square.bind("<Down>", car.move_car)
            square.bind("<Right>", car.move_car)
            square.bind("<Left>", car.move_car)
        window.after(500,_enable_movement())

if __name__ == "__main__":
    window = tk.Tk()
    a = Board(window)
    a.pack()
    a.set_level(1)
    window.mainloop()
