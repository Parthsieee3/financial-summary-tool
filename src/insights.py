
# src/insights.py
import pandas as pd

def top_transactions(df: pd.DataFrame, n:int=10) -> pd.DataFrame:
    return df.reindex(df['amount'].abs().sort_values(ascending=False).index).head(n)

def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    s = df['amount'].abs()
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5*iqr
    upper = q3 + 1.5*iqr
    df = df.copy()
    df['is_anomaly'] = (s < lower) | (s > upper)
    df['is_duplicate'] = df.duplicated(subset=['date','amount','description'], keep=False)
    return df[df['is_anomaly'] | df['is_duplicate']]
