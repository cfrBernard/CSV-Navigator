def export_csv(df, filepath: str):
    df.to_csv(filepath, index=False)


def export_json(df, filepath: str):
    df.to_json(filepath, orient="records", indent=2)
