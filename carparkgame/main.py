import tkinter as tk
from board import Board


if __name__ == "__main__":
    window = tk.Tk()
    game = Board(window)
    game.pack()
    game.set_level(1)
    window.mainloop()
