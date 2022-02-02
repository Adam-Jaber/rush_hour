import tkinter as tk
from login_screen import LoginScreen
from signup_screen import SignupScreen
from main_menu import MainMenu
from levels_screen import LevelsScreen
from board import Board


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.geometry("600x1066")
        self.config(bg="#303030")

        LoginScreen(self).pack()

    def login_screen(self, current_screen):
        current_screen.destroy()
        LoginScreen(self).pack()

    def signup_screen(self, current_screen):
        current_screen.destroy()
        SignupScreen(self,).pack()

    def main_menu(self, user_id, current_screen):
        current_screen.destroy()
        MainMenu(self, user_id).pack()

    def levels_screen(self, user_id, current_screen):
        current_screen.destroy()
        LevelsScreen(self, user_id).pack()

    def play_level(self, level_num, user_id, current_screen):
        current_screen.destroy()
        Board(self, level_num, user_id).pack()

    def winning_screen(self, user_id, current_screen):
        current_screen.destroy()
        winning_frame = tk.Frame(self)
        canvas = tk.Canvas(winning_frame)
        win_gif = tk.PhotoImage(file="you_go_girl.gif")
        canvas.create_image(image=win_gif)
        canvas.pack()
        home_button = tk.Button(winning_frame, width=600, height=100, text="Return to home screen",
                                font=('Helvetica', 50), command=lambda: self.main_menu(user_id, winning_frame))
        home_button.pack()
