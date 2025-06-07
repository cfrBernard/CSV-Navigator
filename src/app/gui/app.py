import customtkinter as ctk

from .components.sidebar_view import SidebarView
from .components.stats_view import StatsView
from .components.table_view import TableView


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CSV Navigator")
        self.geometry("1200x800")
        self.minsize(900, 600)

        # Layout : sidebar | main
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = SidebarView(self)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=0, pady=5)

        # Main section : TableView + StatsView
        main_frame = ctk.CTkFrame(self, corner_radius=0)
        main_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=0)
        main_frame.grid_columnconfigure(0, weight=1)

        self.table_view = TableView(main_frame)
        self.table_view.grid(row=0, column=0, sticky="nsew")

        self.stats_view = StatsView(main_frame)
        self.stats_view.grid(row=1, column=0, sticky="ew", pady=(5, 0))
