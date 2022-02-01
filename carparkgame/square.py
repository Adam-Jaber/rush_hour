import tkinter as tk


class Square(tk.Frame):
    def __init__(self, master, row, column):
        super().__init__(master, width=70, height=70, bg='white', bd=5, relief='sunken')
        self.row = row
        self.column = column
        self.bind('<Button-1>', self.focus_set)

    def focus_set(self, event=None):
        super().focus_set()

    def paint(self, color):
        self.config(bg=color)

    def unpaint(self):
        self.config(bg='white')
