
# src/data_io_save.py
import pandas as pd
from pathlib import Path
import json

def save_json(obj, path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'w', encoding='utf8') as f:
        json.dump(obj, f, default=str, indent=2)

def save_excel(dfs: dict, path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(p, engine='openpyxl') as writer:
        for sheet, df in dfs.items():
            if hasattr(df, 'to_frame') and not isinstance(df, pd.DataFrame):
                df = df.to_frame()
            df.to_excel(writer, sheet_name=sheet[:31], index=True)
