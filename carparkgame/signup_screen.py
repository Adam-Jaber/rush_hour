import tkinter as tk
from tkinter import messagebox


class SignupScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, height=600, width=600 * (16 / 9))

        self.master = master
        self.f_name_var = tk.StringVar()
        self.l_name_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.setup()

    def setup(self):
        tk.Label(self, text="First name:", )