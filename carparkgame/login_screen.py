import psycopg2 as pg
import tkinter as tk
from tkinter import messagebox


class LoginScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, height=600, width=600 * (16/9))

        self.master = master
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.set_up()

    def set_up(self):
        tk.Label(self, text="Username:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.username_var, width=40).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self, text="Password:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.password_var, width=40, show="*").grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self, text="Login", command=self.check_info).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self, text="Sign up", command=lambda: self.master.signup_screen(self)).grid(row=4, column=0,
                                                                                              columnspan=2)

    def check_info(self):
        con = pg.connect(database='rush_hour', user='postgres', password='jaber2213')
        cur = con.cursor()

        try:
            cur.execute(f"""SELECT user_id, user_password=\'{self.password_var.get()}\' FROM users
                            WHERE username=\'{self.username_var.get()}\';""")
            user_info = cur.fetchone()

            if user_info[1]:
                self.master.main_menu(user_info[0], self)
            else:
                messagebox.showinfo("wrong info", "password is incorrect")
        except IndexError:
            messagebox.showinfo("wrong info", f'username {self.username_var.get()} does not exist')
