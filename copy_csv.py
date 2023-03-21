
# This script copy multiple csv files in a folder into a PostgreSQL database

import os
import psycopg2
from psycopg2 import sql

def copy_csv_to_postgresql(csv_folder_path, db_name, db_user, db_password, db_host, db_port):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    cur = conn.cursor()