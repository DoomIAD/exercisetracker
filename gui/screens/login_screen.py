import customtkinter as ctk
from gui.special_functions.date_formatter import *

class Login_Screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.switch_var = ctk.StringVar(value="Male")
        

        ctk.CTkLabel(self, text="Login").pack(pady=10)


        # Weight
        ctk.CTkLabel(self, text="Weight").pack(pady=5)

        self.weight_var = ctk.StringVar(value="50.0")

        self.weight_entry = ctk.CTkEntry(self, textvariable=self.weight_var, width=80)
        self.weight_entry.pack()

        self.weight_slider = ctk.CTkSlider(
            self,
            from_=500,
            to=2500,
            number_of_steps=2000,
            command=self.update_weight_label
        )
        self.weight_slider.pack()

        self.weight_entry.bind("<KeyRelease>", self.update_slider_from_entry)

        # Height
        ctk.CTkLabel(self, text="Height").pack(pady=10)
        self.height_value_label = ctk.CTkLabel(self, text="0")
        self.height_value_label.pack()
        height_slider = ctk.CTkSlider(
            self,
            from_=24,   # 2'0"
            to=108,     # 9'0"
            command=self.update_height_label
        )
        height_slider.pack()

        # Birthdate
        ctk.CTkLabel(self, text="Birthdate").pack(pady=10)
        birth_date_entry = BirthdateEntry(self, placeholder_text="MM/DD/YYYY")
        birth_date_entry.pack()

        # Gender
        ctk.CTkLabel(self, text="Gender").pack(pady=10)

        self.genderswitch = ctk.CTkSwitch(
            self,
            text=self.switch_var.get(),
            command=self.update_gender_label,
            variable=self.switch_var,
            onvalue="Female",
            offvalue="Male"
        )
        self.genderswitch.pack()

    def update_weight_label(self, value):
        weight = float(value) / 10
        self.weight_var.set(f"{weight:.1f}")

    def update_slider_from_entry(self, event=None):
        try:
            value = float(self.weight_var.get())
            self.weight_slider.set(value * 10)
        except ValueError:
            pass
        
    def update_height_label(self, value):
        total_inches = int(value)
        feet = total_inches // 12
        inches = total_inches % 12
        self.height_value_label.configure(text=f"{feet}'{inches}\"")
    
    def update_gender_label(self):
        gender = self.switch_var.get()
        self.genderswitch.configure(text=gender)
