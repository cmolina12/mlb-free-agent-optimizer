import sqlite3
import pandas as pd
from .config import DB_PATH


def get_connection():
    """
    Open a connection to the main SQLite DB.
    Use with 'with get_connection() as conn:' so it closes automatically.
    """
    return sqlite3.connect(DB_PATH)


def load_hitting_table() -> pd.DataFrame:
    """
    Return the full 'hitting' table from merged.db as a pandas DataFrame.
    """
    with get_connection() as conn:
        return pd.read_sql("SELECT * FROM hitting", conn)
