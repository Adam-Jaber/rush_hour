import hashlib
import requests
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
        salt_info = requests.get(f"""https://2rc2iohsvl.execute-api.us-east-2.amazonaws.com/test/users?username={self.username_var.get()}&columns=salt""").json()
        try:
            salt = salt_info[0].encode('utf-8')
        except IndexError:
            messagebox.showinfo("wrong info", f'username {self.username_var.get()} does not exist')
            return

        hashed_pass = hashlib.pbkdf2_hmac('sha256', self.password_var.get().encode('utf-8'), salt, 100000)
        user_info = requests.get(f"""https://2rc2iohsvl.execute-api.us-east-2.amazonaws.com/test/users?username={self.username_var.get()}&columns=user_id,user_password""").json()

        if user_info[1] == hashed_pass.hex():
            self.master.main_menu(user_info[0], self)
        else:
            messagebox.showinfo("wrong info", "password is incorrect")
