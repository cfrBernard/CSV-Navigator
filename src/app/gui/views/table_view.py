from tkinter import ttk

import customtkinter as ctk
import pandas as pd
from customtkinter import CTkScrollbar


class TableView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.tree = None
        self._build_ui()

        style = ttk.Style()
        style.theme_use("clam")

        # Treeview
        style.configure(
            "Treeview",
            background="#1e1e1e",
            foreground="#bbbbbb",
            fieldbackground="#1e1e1e",
            rowheight=25,
            borderwidth=0,
            relief="flat",
        )

        # Heading
        style.configure(
            "Treeview.Heading",
            background="#2b2b2b",
            foreground="#c5c5c5",
            font=("Arial", 12, "bold"),
            borderwidth=0,
        )

        style.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])

    def _build_ui(self):
        container = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=0)
        container.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(container, show="headings")
        vsb = CTkScrollbar(container, orientation="vertical", command=self.tree.yview)

        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

    def update_table(self, df: pd.DataFrame):
        # Reset current table
        for col in self.tree.get_children():
            self.tree.delete(col)
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(df.columns)

        # Set column headings
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        # Insert rows
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))
