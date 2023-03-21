
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

    
    # Loop through each CSV file in the folder
    for filename in os.listdir(csv_folder_path):
        if filename.endswith('.csv'):
            # Open the CSV file and read the contents
            with open(os.path.join(csv_folder_path, filename), 'r') as f:
                # Create a temporary table to hold the CSV data
                cur.execute('CREATE TEMP TABLE tmp_table (LIKE {} INCLUDING ALL)'.format(sql.Identifier(filename[:-4])))
                # Load the CSV data into the temporary table
                cur.copy_expert('COPY tmp_table FROM STDIN WITH CSV HEADER', f)
                # Insert the data from the temporary table into the destination table
                cur.execute('INSERT INTO {} SELECT * FROM tmp_table'.format(sql.Identifier(filename[:-4])))
                # Drop the temporary table
                cur.execute('DROP TABLE tmp_table')

    # Commit the changes and close the connection
    conn.commit()
    cur.close()
    conn.close()