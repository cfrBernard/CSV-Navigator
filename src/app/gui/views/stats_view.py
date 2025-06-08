import customtkinter as ctk


class StatsView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(height=250, corner_radius=0)
        self.grid_propagate(False)
