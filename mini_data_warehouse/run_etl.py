from etl.extract import extract_csv
from etl.transform import clean_data
from etl.load import load_to_sqlite

def run_etl():
    df = extract_csv()
    df_clean = clean_data(df)
    load_to_sqlite(df_clean)
    print('ETL completed successfully!')

if __name__=='__main__':
    run_etl()
