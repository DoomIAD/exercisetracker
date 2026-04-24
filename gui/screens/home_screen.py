import customtkinter as ctk

class Home_Screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        ctk.CTkLabel(self, text="Home").pack(pady=20)

        ctk.CTkButton(
            self,
            text="Back to Frame 1",
            command=lambda: controller.show_frame("Frame1")
        ).pack()