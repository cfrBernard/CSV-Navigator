import customtkinter as ctk


class TableView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(corner_radius=0)

    def update_table(self, dataframe):
        # Implémenter la logique pour afficher le DataFrame
        pass
