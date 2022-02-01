import tkinter as tk
from tkinter import messagebox
import psycopg2 as pg

class SignupScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master, height=600, width=600 * (16 / 9))

        self.master = master
        self.f_name_var = tk.StringVar()
        self.l_name_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.repassword_var = tk.StringVar()

        self.setup()

    def setup(self):
        tk.Label(self, text="Sign Up:", font=('Helvetica',35)).grid(row=0, column=0, pady=120)

        tk.Label(self, text="First name:").grid(row=1, column=0, pady=40, padx=60)
        tk.Entry(self, textvariable=self.f_name_var, width=40).grid(row=1, colum=1, pady=40, padx=60)

        tk.Label(self, text="Last name:").grid(row=2, column=0, pady=40, padx=60)
        tk.Entry(self, textvariable=self.l_name_var, width=40).grid(row=2, column=1, pady=40, padx=60)

        tk.Label(self, text="Username:").grid(row=3, column=0, pady=40, padx=60)
        tk.Entry(self, textvariable=self.username_var, width=40).grid(row=3, column=1, pady=40, padx=60)

        tk.Label(self, text="Password:").grid(row=4, column=0, pady=40, padx=60)
        tk.Entry(self, textvariable=self.password_var, width=40, show="*").grid(row=4, column=1, pady=40, padx=60)

        tk.Label(self, text="Confirm password:").grid(row=5, column=0, pady=40, padx=60)
        tk.Entry(self, textvariable=self.repassword_var, width=40).grid(row=5, colum=1, pady=40, padx=60)

        tk.Button(self, text="Confirm", command=self.check_info).grid(row=6, column=0, columnspan=2, pady=60)

    def check_info(self):
        con = pg.connect(database='rush_hour', user='postgres', password='jaber2213')
        cur = con.cursor()
        cur.execute(f'SELECT * FROM users WHERE username = {self.username_var.get()}')
        try:
            for var in (self.f_name_var,self.l_name_var,self.username_var,self.password_var):
                assert var.get() != ""
            if not self.f_name_var.get().isalpha():
                raise game_errors.InvalidFName
            if not self.l_name_var.get().isalpha():
                raise game_errors.InvalidLName
            if len(cur.fetchone()) =! 0:
                raise game_errors.UsernameExists
            if self.password_var.get() =! self.repassword_var.get():
                raise game_errors.PasswordConfirmError
            SignupScreen.check_password(self.password_var.get())
        except AssertionError:
            messagebox.showerror("empty field", "please fill all the sections")
        except game_errors.InvalidFName:
            messagebox.showerror("incorrect info", "first name can only contain letters")
        except game_errors.InvalidLName:
            messagebox.showerror("incorrect info", "last name can only contain letters")
        except game_errors.UsernameExists:
            messagebox.showinfo("username error", "the username you chose already exists")
        except game_errors.PasswordConfirmError:
            messagebox.showerror("password error", "the password confirmation is incorrect")
        except game_error.PasswordError:
            messagebox.showerror("password error", "your password does not comply with the restrictions")
        else:
            cur.execute(f'INSERT INTO users'
                        f'Values({self.username_var.get()},{self.password_var.get()},'
                        f'{self.f_name_var.get()},{self.l_name_var.get()})'
            cur.commit()
            self.master.login_screen()
        return

    @staticmethod
    def check_password(password):
        if len(password) > 32 or len(password) < 8:
            raise game_error.PasswordError
        if password.isalpha():
            raise game_error.PasswordError
        if not any(c.isalpha() for c in password):
            raise game_error.PasswordError
        return