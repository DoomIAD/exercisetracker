import customtkinter as ctk

class Create_Exercise_Screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        ctk.CTkLabel(self, text="Create Exercise").pack(pady=20)

        ctk.CTkButton(
            self,
            text="Go to Frame 2",
            command=lambda: controller.show_frame("Frame2")
        ).pack()