from tkinter import filedialog, messagebox

import customtkinter as ctk


class ImportTool(ctk.CTkFrame):
    def __init__(self, parent, on_import_callback=None):
        super().__init__(parent)

        self.current_file = None  # Track du fichier
        self.on_import_callback = on_import_callback

        self.configure(corner_radius=0)
        self.button = ctk.CTkButton(self, text="Open CSV", command=self.import_file)
        self.button.pack(fill="x", padx=10, pady=10)

    def import_file(self):
        # demande confirmation
        if self.current_file:
            confirm = messagebox.askyesno(
                "Replace CSV ?",
                "A CSV file is already uploaded.\nAre you sure you want to upload a new one ?",
            )
            if not confirm:
                return

        # Sélection du fichier
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.current_file = file_path
            print(f"[ImportTool] New import : {file_path}")

            if self.on_import_callback:
                self.on_import_callback(file_path)
