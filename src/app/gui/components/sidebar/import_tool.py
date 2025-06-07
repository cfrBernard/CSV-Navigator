from tkinter import filedialog

import customtkinter as ctk


class ImportTool(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(corner_radius=0)
        self.button = ctk.CTkButton(self, text="Open CSV", command=self.import_file)
        self.button.pack(fill="x", padx=10, pady=10)

    def import_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            print(f"Import CSV : {file_path}")
            # envoyer path à contrôleur ou signaler
