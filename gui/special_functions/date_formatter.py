import customtkinter as ctk

class BirthdateEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        self.var = ctk.StringVar()
        super().__init__(master, textvariable=self.var, **kwargs)

        self.bind("<KeyRelease>", self.format_date)

    def format_date(self, event=None):
        text = self.var.get()

        # Remove anything that's not a digit
        digits = "".join(c for c in text if c.isdigit())

        # Limit to 8 digits (MMDDYYYY)
        digits = digits[:8]

        # Build formatted string
        result = ""
        if len(digits) > 0:
            result += digits[:2]
        if len(digits) >= 3:
            result += "/" + digits[2:4]
        if len(digits) >= 5:
            result += "/" + digits[4:]

        # Prevent cursor jump issues
        self.var.set(result)