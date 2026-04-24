import customtkinter as ctk

from .screens.create_exercise_screen import Create_Exercise_Screen
from .screens.login_screen import Login_Screen
from .screens.home_screen import Home_Screen


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Exercise Tracker")
        self.geometry("400x300")

        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Create and store frames
        for F in (Create_Exercise_Screen, Login_Screen, Home_Screen):
            frame = F(container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start screen (choose logically)
        self.show_frame("Login_Screen")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()