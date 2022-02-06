import hashlib
import tkinter as tk
from os import urandom
from tkinter import messagebox
import psycopg2 as pg
import game_exceptions


class SignupScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, height=600, width=1066)
        self.master = master
        self.f_name_var = tk.StringVar()
        self.l_name_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.repassword_var = tk.StringVar()

        self.setup()

    def setup(self):
        tk.Label(self, text="Sign Up:", font=('Helvetica', 35)).grid(row=0, column=0, pady=60)

        tk.Label(self, text="First name:").grid(row=1, column=0, pady=20, padx=60)
        tk.Entry(self, textvariable=self.f_name_var, width=40).grid(row=1, column=1, pady=20, padx=60)

        tk.Label(self, text="Last name:").grid(row=2, column=0, pady=20, padx=60)
        tk.Entry(self, textvariable=self.l_name_var, width=40).grid(row=2, column=1, pady=20, padx=60)

        tk.Label(self, text="Username:").grid(row=3, column=0, pady=20, padx=60)
        tk.Entry(self, textvariable=self.username_var, width=40).grid(row=3, column=1, pady=20, padx=60)

        tk.Label(self, text="Password:").grid(row=4, column=0, pady=20, padx=60)
        tk.Entry(self, textvariable=self.password_var, width=40, show="*").grid(row=4, column=1, pady=20, padx=60)
        tk.Label(self, font=("Ariel", 7), text="""must contain:
                               at least 8 characters and up to 32
                               one alphabet char.
                               one number or special digit""").grid(row=4, column=2, padx=10, pady=20)

        tk.Label(self, text="Confirm password:").grid(row=5, column=0, pady=20, padx=60)
        tk.Entry(self, textvariable=self.repassword_var, width=40, show="*").grid(row=5, column=1, pady=20, padx=60)

        tk.Button(self, text="Confirm", command=self.check_info).grid(row=6, column=0, columnspan=2, pady=30)

    def check_info(self):
        con = pg.connect(database='rush_hour', user='postgres', password='jaber2213')
        cur = con.cursor()
        cur.execute(f'SELECT * FROM users WHERE username = \'{self.username_var.get()}\'')
        try:
            for var in (self.f_name_var, self.l_name_var, self.username_var, self.password_var):
                assert var.get() != ""

            if not self.f_name_var.get().isalpha():
                raise game_exceptions.InvalidFName

            if not self.l_name_var.get().isalpha():
                raise game_exceptions.InvalidLName

            if len(cur.fetchall()) != 0:
                raise game_exceptions.UsernameExists

            if self.password_var.get() != self.repassword_var.get():
                raise game_exceptions.ConfirmError

            SignupScreen.check_password(self.password_var.get())
        except AssertionError:
            messagebox.showerror("empty field", "please fill all the sections")
        except game_exceptions.SignupException as e:
            messagebox.showerror("signup error", e)
        else:
            self.store_info()
        return

    def store_info(self):
        salt = urandom(16).hex()
        hashed_pass = hashlib.pbkdf2_hmac('sha256', self.password_var.get().encode('utf-8'), salt.encode('utf-8'), 100000)

        con = pg.connect(database='rush_hour', user='postgres', password='jaber2213')
        cur = con.cursor()
        cur.execute(f"""INSERT INTO users (username, user_password, salt, first_name, last_name)
                        Values(\'{self.username_var.get()}\',\'{hashed_pass.hex()}\',
                        \'{salt}\',\'{self.f_name_var.get()}\',\'{self.l_name_var.get()}\')""")
        con.commit()

        self.master.login_screen(self)

    @staticmethod
    def check_password(password):
        if len(password) > 32 or len(password) < 8:
            raise game_exceptions.InvalidPassword
        if password.isalpha():
            raise game_exceptions.InvalidPassword
        if not any(c.isalpha() for c in password):
            raise game_exceptions.InvalidPassword
        return
