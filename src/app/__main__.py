import customtkinter as ctk

from app.core.controller import AppController


def main():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    controller = AppController()
    controller.run()


if __name__ == "__main__":
    main()
