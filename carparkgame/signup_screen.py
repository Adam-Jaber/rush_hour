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

        tk.Button(self, text="Confirm", command=self.checkinfo).grid(row=6, column=0, columnspan=2, pady=60)
