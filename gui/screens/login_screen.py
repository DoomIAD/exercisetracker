import customtkinter as ctk
from PIL import Image
from gui.special_functions.date_formatter import *


class Login_Screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.switch_var = ctk.StringVar(value="Male")
        
        # Configure the grid layout for the screen
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=4)
        self.bind("<Configure>", self._on_resize)

        frame_left = ctk.CTkFrame(self)
        frame_left.grid(row=0, column=0, sticky="nsew", padx=(20, 10), pady=20)

        self.frame_right = ctk.CTkFrame(self)
        self.frame_right.grid(row=0, column=1, sticky="nsew", padx=(10, 20), pady=20)
        self.bind("<Configure>", self._on_image_resize)


        # Rock Image
        self.base_image = Image.open("gui/assets/rock_male.png")

        self.my_image = ctk.CTkImage(
            light_image=self.base_image,
            dark_image=self.base_image,
            size=(256, 256)
        )
        self.image_label = ctk.CTkLabel(self.frame_right, image=self.my_image, text="")
        self.image_label.pack(expand=True, padx=20, pady=20)
        
        # Weight
        ctk.CTkLabel(frame_left, text="Weight").pack(pady=5)

        self.weight_var = ctk.StringVar(value="50.0")

        self.weight_entry = ctk.CTkEntry(frame_left, textvariable=self.weight_var, width=80)
        self.weight_entry.pack(padx=20, fill="x")

        self.weight_slider = ctk.CTkSlider(
            frame_left,
            from_=500,
            to=2500,
            number_of_steps=2000,
            command=self.update_weight_label
        )
        self.weight_slider.pack(padx=20, fill="x")

        self.weight_entry.bind("<KeyRelease>", self.update_slider_from_entry)

        # Height
        ctk.CTkLabel(frame_left, text="Height").pack(pady=10)
        self.height_value_label = ctk.CTkLabel(frame_left, text="0")
        self.height_value_label.pack()
        self.height_slider = ctk.CTkSlider(
            frame_left,
            from_=24,   # 2'0"
            to=108,     # 9'0"
            command=self.update_height_label
        )
        self.height_slider.pack(padx=20, fill="x")

        # Birthdate
        ctk.CTkLabel(frame_left, text="Birthdate").pack(pady=10)
        birth_date_entry = BirthdateEntry(frame_left, placeholder_text="MM/DD/YYYY")
        birth_date_entry.pack(padx=20, fill="x")

        # Gender
        ctk.CTkLabel(frame_left, text="Gender").pack(pady=10)

        self.genderswitch = ctk.CTkSwitch(
            frame_left,
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
        self._on_image_resize()

    def update_slider_from_entry(self, event=None):
        try:
            value = float(self.weight_var.get())
            self.weight_slider.set(value * 10)
            self._on_image_resize()
        except ValueError:
            pass
        
    def update_height_label(self, value):
        total_inches = int(value)
        feet = total_inches // 12
        inches = total_inches % 12
        self.height_value_label.configure(text=f"{feet}'{inches}\"")
        self._on_image_resize()
    
    def update_gender_label(self):
        gender = self.switch_var.get()
        self.genderswitch.configure(text=gender)

    def _on_resize(self, event):
        """Handles responsive logic to cap the left frame at 480px."""
        if event.widget == self:
            # If the screen is wide enough that a 50/50 split exceeds 480px
            if event.width > 960:
                self.grid_columnconfigure(0, weight=0, minsize=480)
                self.grid_columnconfigure(1, weight=1)
            else:
                # Otherwise, let them scale proportionally
                self.grid_columnconfigure(0, weight=1, minsize=0)
                self.grid_columnconfigure(1, weight=1)

    def _on_image_resize(self, event=None):
        """Resize image dynamically based on available space, weight, and height."""

        # Get right frame size directly (more stable than event.widget)
        width = self.frame_right.winfo_width()
        height = self.frame_right.winfo_height()

        # Ignore invalid dimensions during initialization
        if width < 100 or height < 100:
            return

        try:
            # Weight factor (influences width)
            weight = float(self.weight_var.get())
            width_factor = weight / 150.0
            width_factor = max(0.4, min(width_factor, 2.5))

            # Height factor (influences height)
            if hasattr(self, 'height_slider'):
                height_val = float(self.height_slider.get())
                height_factor = height_val / 70.0  # 70 inches is used as the baseline
                height_factor = max(0.4, min(height_factor, 2.5))
            else:
                height_factor = 1.0
        except (ValueError, AttributeError):
            width_factor = 1.0
            height_factor = 1.0

        base_size = min(width, height) * 0.6
        if base_size < 10:
            return

        self.my_image = ctk.CTkImage(
            light_image=self.base_image,
            dark_image=self.base_image,
            size=(int(base_size * width_factor), int(base_size * height_factor))
        )

        self.image_label.configure(image=self.my_image)