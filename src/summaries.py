
# src/summaries.py
import pandas as pd

def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['year_month'] = df['date'].dt.to_period('M')
    grouped = df.groupby('year_month')['amount'].agg(total='sum', count='count')
    income = df[df['amount'] > 0].groupby('year_month')['amount'].sum().rename('income')
    expense = df[df['amount'] < 0].groupby('year_month')['amount'].sum().rename('expense')
    result = pd.concat([grouped, income, expense], axis=1).fillna(0)
    result['net'] = result['income'] + result['expense']
    result.index = result.index.astype(str)
    return result.reset_index().rename(columns={'year_month': 'period'})

def category_summary(df: pd.DataFrame, top_n:int=20) -> pd.DataFrame:
    grouped = df.groupby('category')['amount'].sum().abs().sort_values(ascending=False).head(top_n)
    total = grouped.sum()
    out = grouped.reset_index().rename(columns={0:'amount'})
    out.columns = ['category','amount']
    out['percent_of_top'] = (out['amount'] / total * 100).round(2)
    return out
