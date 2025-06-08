from app.core.dataloader import load_csv
from app.main_app import MainApp


class AppController:
    def __init__(self):
        self.df = None
        self.app = MainApp()

        # ImportTool callback
        self.app.sidebar.import_tool.on_import_callback = self.on_csv_imported

    def on_csv_imported(self, file_path: str):
        try:
            self.df = load_csv(file_path)
            print(f"[Controller] CSV loaded, shape: {self.df.shape}")
            self.app.table_view.update_table(self.df)
            self.app.stats_view.update_stats(self.df)
        except Exception as e:
            print(f"[Controller] Failed to import CSV: {e}")

    def run(self):
        self.app.mainloop()
