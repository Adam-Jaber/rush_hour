import tkinter as tk
import requests




class LevelsScreen(tk.Frame):
    def __init__(self, master, user_id):
        super(LevelsScreen, self).__init__(master, width=600, height=600 * (16/9))

        self.user_id = user_id
        self.button_dict = dict()

        self.set_up()

    def set_up(self):
        self.pack_lvl_buttons()
        self.disable_unreached_lvl()

    def pack_lvl_buttons(self):
        levels_list = requests.get("https://2rc2iohsvl.execute-api.us-east-2.amazonaws.com/test/level_info").json()
        for level_num in levels_list:
            button = tk.Button(self, text=str(level_num), font=('Helvetica', 30),
                               state=tk.DISABLED, bg="#404040")
            button.grid(row=level_num // 5, column=level_num % 5, padx=30, pady=30)
            self.button_dict[level_num] = button

    def disable_unreached_lvl(self):
        passed_levels_list = requests.get(f"https://2rc2iohsvl.execute-api.us-east-2.amazonaws.com/test/passed_levels?user_id={self.user_id}").json()
        for lvl_num in passed_levels_list:
            self.button_dict[lvl_num].configure(state=tk.NORMAL, bg="#C0C0C0", command=lambda: self.play_level(lvl_num))
            try:
                self.button_dict[lvl_num + 1].configure(state=tk.NORMAL, bg="#C0C0C0",
                                                        command=lambda: self.play_level(lvl_num + 1))
            except KeyError:
                pass
        self.button_dict[1].config(state=tk.NORMAL, bg="#C0C0C0", command=lambda: self.play_level(1))

    def play_level(self, level_num):
        self.master.play_level(level_num, self.user_id, self)
