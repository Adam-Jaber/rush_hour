import tkinter as tk


class MainMenu(tk.Frame):
    def __init__(self, master, user_id):
        self.user_id = user_id
        self.master = master
        super().__init__(master, height=600, width=600 * (16/9), bg="#707070")

        self.setup()

    def setup(self):
        gif_canvas = tk.Canvas(self, height=400, width=1066)
        open("lig_mcqueen.png", 'r')
        photo = tk.PhotoImage("lig_mcqueen.png")
        gif_canvas.create_image(500, 0, image=photo, anchor='n')
        gif_canvas.place(x=0, y=0)

        tk.Button(self, text="Play", font=('Helvetica', 35), command=self.play,
                  bg="#B0B0B0").place(y=470, x=533, anchor='n')

    def play(self):
        self.master.levels_screen(self.user_id, self)
