from tkinter import ttk

import customtkinter as ctk
import pandas as pd
from customtkinter import CTkScrollbar


class TableView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.tree = None
        self.df = pd.DataFrame()
        self.page = 1
        self.page_size = 50
        self.sort_column = None
        self.sort_reverse = False

        self._build_ui()

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="#1e1e1e",
            foreground="#bbbbbb",
            fieldbackground="#1e1e1e",
            rowheight=25,
            borderwidth=0,
            relief="flat",
        )

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

        # Barre de pagination / recherche
        control_frame = ctk.CTkFrame(container, fg_color="transparent")
        control_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5, padx=10)

        self.search_entry = ctk.CTkEntry(control_frame, placeholder_text="🔍 Search...", width=200)
        self.search_entry.pack(side="left", padx=5)
        self.search_entry.bind("<Return>", self.search)

        reset_btn = ctk.CTkButton(control_frame, text="↻ Reset", width=60, command=self.reset_view)
        reset_btn.pack(side="left", padx=5)

        self.next_btn = ctk.CTkButton(control_frame, text="▶", width=30, command=self.next_page)
        self.next_btn.pack(side="right", padx=2)

        self.page_label = ctk.CTkLabel(control_frame, text="Page 1")
        self.page_label.pack(side="right", padx=5)

        self.prev_btn = ctk.CTkButton(control_frame, text="◀", width=30, command=self.prev_page)
        self.prev_btn.pack(side="right", padx=2)

    def update_table(self, df: pd.DataFrame):
        self.df = df.copy()
        self.page = 1
        self.sort_column = None
        self.sort_reverse = False
        self._load_page()

    def _load_page(self):
        if self.sort_column:
            self.df = self.df.sort_values(by=self.sort_column, ascending=not self.sort_reverse)

        df_page = self.df.iloc[(self.page - 1) * self.page_size : self.page * self.page_size]

        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(self.df.columns)

        for col in self.df.columns:
            heading = col
            if col == self.sort_column:
                heading += " ▼" if self.sort_reverse else " ▲"
            self.tree.heading(col, text=heading, command=lambda _col=col: self.sort_by_column(_col))
            self.tree.column(col, width=100, anchor="center")

        for _, row in df_page.iterrows():
            self.tree.insert("", "end", values=list(row))

        self.page_label.configure(text=f"Page {self.page}")
        self.prev_btn.configure(state="normal" if self.page > 1 else "disabled")
        self.next_btn.configure(
            state="normal" if self.page * self.page_size < len(self.df) else "disabled"
        )

    def next_page(self):
        if self.page * self.page_size < len(self.df):
            self.page += 1
            self._load_page()

    def prev_page(self):
        if self.page > 1:
            self.page -= 1
            self._load_page()

    def sort_by_column(self, col):
        if self.sort_column == col:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_reverse = False
            self.sort_column = col
        self.page = 1
        self._load_page()

    def search(self, event=None):
        query = self.search_entry.get().lower()
        if query.strip() == "":
            return
        mask = self.df.apply(
            lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1
        )
        filtered_df = self.df[mask]
        self.update_table(filtered_df)

    def reset_view(self):
        self.search_entry.delete(0, "end")
        self.page = 1
        self.sort_column = None
        self.sort_reverse = False
        self._load_page()
