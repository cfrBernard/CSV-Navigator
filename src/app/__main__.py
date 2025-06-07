import customtkinter as ctk

from app.gui.app import MainApp

if __name__ == "__main__":

    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    app = MainApp()
    app.mainloop()
