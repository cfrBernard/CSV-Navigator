import customtkinter as ctk


def main():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("CSV-Navigator")
    app.geometry("900x600")

    # TODO : Setup interface + onglets

    app.mainloop()
