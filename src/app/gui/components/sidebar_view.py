import customtkinter as ctk


class SidebarView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(corner_radius=0)
