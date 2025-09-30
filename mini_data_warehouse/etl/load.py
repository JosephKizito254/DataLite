import sqlite3

def load_to_sqlite(df, db_path='db/warehouse.db', table_name='sales'):
    """Load dataframe to SQLite database"""
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
