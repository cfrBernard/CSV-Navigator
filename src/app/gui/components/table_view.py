from tkinter import ttk
from typing import Any

import customtkinter as ctk


class TableView(ctk.CTkFrame):
    def __init__(self, master: Any | None = None, **kwargs: Any) -> None:
        super().__init__(master, **kwargs)
        self.tree = ttk.Treeview(self)
        self.tree.pack(expand=True, fill="both")
        # TODO : Setup colonnes, scrollbars, etc
