
import pandas as pd
from src.data_io import load_transactions
from src.cleaning import clean_transactions

def test_load_and_clean():
    df = load_transactions("financial_transactions (1).csv")
    df2 = clean_transactions(df)
    assert 'amount' in df2.columns
