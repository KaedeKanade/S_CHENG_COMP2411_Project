import psycopg2
from psycopg2 import sql
from Config import DB_CONFIG,default_config

cursor = None
conn = None

try:
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(**default_config)

    
    conn.autocommit = True  # Enable autocommit mode

    # Create a cursor object
    cursor = conn.cursor()

    # Create a new database
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_CONFIG['dbname'])))

    print(f"Database '{DB_CONFIG['dbname']}' created successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and conn
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()