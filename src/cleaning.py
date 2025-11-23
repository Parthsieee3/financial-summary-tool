
# src/cleaning.py
import pandas as pd

def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    amt_cols = [c for c in df.columns if 'amount' in c or 'value' in c]
    if amt_cols:
        df['amount'] = pd.to_numeric(df[amt_cols[0]].astype(str).str.replace('[^0-9.-]', '', regex=True), errors='coerce')
    else:
        df['amount'] = pd.to_numeric(df.iloc[:, -1], errors='coerce')

    if 'category' not in df.columns:
        df['category'] = df.get('description', '').str.lower().fillna('uncategorized')

    df = df.dropna(subset=['date', 'amount'], how='any')
    df['category'] = df['category'].astype(str).str.strip().str.title()
    return df
