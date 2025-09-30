import time
from run_etl import run_etl

def schedule_etl(interval_seconds=86400):
    """Run ETL periodically"""
    while True:
        print('Running scheduled ETL...')
        run_etl()
        print('ETL completed. Sleeping until next run.')
        time.sleep(interval_seconds)

if __name__=='__main__':
    schedule_etl(60)  # runs every 60 seconds for demo
