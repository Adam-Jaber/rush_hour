import tkinter as tk
import mysql.connector




class LevelsScreen(tk.Frame):
    def __init__(self, master, user_id):
        super(LevelsScreen, self).__init__(master, width=600, height=600 * (16/9))

        self.user_id = user_id
        self.button_dict = dict()

        self.con = mysql.connector.connect(host='rush-hour.cqc4hsepuzva.us-east-2.rds.amazonaws.com', database='rush_hour',
                                      user='admin', password='rush1234')
        self.cur = self.con.cursor()

        self.set_up()

    def set_up(self):
        self.pack_lvl_buttons()
        self.disable_unreached_lvl()

    def pack_lvl_buttons(self):
        self.cur.execute("Select level_num FROM levels")
        for level in self.cur.fetchall():
            level_num = level[0]
            button = tk.Button(self, text=str(level_num), font=('Helvetica', 30),
                               state=tk.DISABLED, bg="#404040")
            button.grid(row=level_num // 5, column=level_num % 5, padx=30, pady=30)
            self.button_dict[level_num] = button

    def disable_unreached_lvl(self):
        self.cur.execute("""select level_num FROM levels
                       JOIN user_level_passed ON
                       levels.level_id = user_level_passed.level_id
                       WHERE user_id={}""".format(self.user_id))
        for line in self.cur.fetchall():
            lvl_num = line[0]
            self.button_dict[lvl_num].configure(state=tk.NORMAL, bg="#C0C0C0", command=lambda: self.play_level(lvl_num))
            try:
                self.button_dict[lvl_num + 1].configure(state=tk.NORMAL, bg="#C0C0C0",
                                                        command=lambda: self.play_level(lvl_num + 1))
            except KeyError:
                pass
        self.button_dict[1].config(state=tk.NORMAL, bg="#C0C0C0", command=lambda: self.play_level(1))

    def play_level(self, level_num):
        self.master.play_level(level_num, self.user_id, self)
