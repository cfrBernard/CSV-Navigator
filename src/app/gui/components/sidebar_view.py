import customtkinter as ctk

from .sidebar.import_tool import ImportTool


class SidebarView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0)
        self.grid_rowconfigure("all", weight=0)
        self.grid_propagate(False)

        # sidebarTools
        self.import_tool = ImportTool(self)
        self.import_tool.pack(fill="x", pady=(0, 0))
