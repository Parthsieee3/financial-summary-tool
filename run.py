
# run.py
import argparse
from src.data_io import load_transactions
from src.cleaning import clean_transactions
from src.summaries import monthly_summary, category_summary
from src.insights import top_transactions, detect_anomalies
from src.data_io_save import save_json, save_excel
from pathlib import Path

def build_reports(input_path: str, outdir: str):
    df = load_transactions(input_path)
    df = clean_transactions(df)
    msum = monthly_summary(df)
    csum = category_summary(df)
    top = top_transactions(df, n=10)
    anomalies = detect_anomalies(df)

    Path(outdir).mkdir(parents=True, exist_ok=True)
    excel_path = Path(outdir)/'financial_summary.xlsx'
    save_excel({
        'monthly_summary': msum,
        'category_summary': csum,
        'top_transactions': top,
        'anomalies': anomalies
    }, excel_path)
    json_obj = {
        'monthly_summary': msum.to_dict(orient='records'),
        'category_summary': csum.to_dict(orient='records'),
        'top_transactions': top.to_dict(orient='records'),
        'anomalies': anomalies.to_dict(orient='records'),
    }
    save_json(json_obj, Path(outdir)/'financial_summary.json')
    print(f"Saved Excel to {excel_path} and JSON to {Path(outdir)/'financial_summary.json'}")
    return excel_path, Path(outdir)/'financial_summary.json'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Financial Transactions Summary Tool')
    parser.add_argument('--input', required=True, help='Path to transactions CSV')
    parser.add_argument('--outdir', default='outputs', help='Output directory')
    args = parser.parse_args()
    build_reports(args.input, args.outdir)
