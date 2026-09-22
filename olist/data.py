import pandas as pd
from pathlib import Path


class Olist:
    def get_data(self):
        csv_path = Path("~/.workintech/olist/data/csv").expanduser()
        file_paths = list(csv_path.iterdir())
        file_names = [path.name for path in file_paths]
        key_names = [
            name.replace("_dataset.csv", "").replace(".csv", "").replace("olist_", "")
            for name in file_names
        ]
        data = {key: pd.read_csv(path) for key, path in zip(key_names, file_paths)}
        return data
