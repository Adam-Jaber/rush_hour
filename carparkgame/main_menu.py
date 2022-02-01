import tkinter as tk
import cloudinary

cloudinary.config(
  cloud_name="adamj",
  api_key="826397975378178",
  api_secret="TLVdvPktUWsG8GlbdiK8cv5B_-I"
)


class MainMenu(tk.Frame):
    def __init__(self, master, user_id):
        self.user_id = user_id
        self.master = master
        super().__init__(master, height=600, width=600 * (16/9), bg="#707070")

        self.setup()

    def setup(self):
        gif_canvas = tk.Canvas(self, height=400, width=600 * (16/9), bg="#B0B0B0")
        gif = tk.PhotoImage(file=cloudinary.CloudinaryImage("cruisin_.gif").image(width=400, height=400, crop="scale"))
        gif_canvas.create_image((400 * (16/9))//2, 0, image=gif, anchor='N')
        gif_canvas.place(x=0, y=0)
        tk.Button(self, width=150, height=60, text="Play", command=self.play, bg="#B0B0B0").place(y=470, x=533,
                                                                                                  anchor='N')

    def play(self):
        self.master.level_screen(self.user_id)
