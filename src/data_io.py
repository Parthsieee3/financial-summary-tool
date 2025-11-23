
# src/data_io.py
from pathlib import Path
import pandas as pd

def load_transactions(path: str) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    df = pd.read_csv(p)
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    for col in ['date', 'transaction_date', 'posted_date']:
        if col in df.columns:
            df['date'] = pd.to_datetime(df[col], errors='coerce')
            break
    if 'date' not in df.columns:
        try:
            df['date'] = pd.to_datetime(df.iloc[:,0], errors='coerce')
        except Exception:
            df['date'] = pd.NaT
    return df
