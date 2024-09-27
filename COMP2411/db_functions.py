import psycopg2
from Config import DB_CONFIG

def create_connection():
    return psycopg2.connect(**DB_CONFIG)


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Guest (
        GuestID SERIAL PRIMARY KEY,
        FirstName VARCHAR(100),
        LastName VARCHAR(100),
        Email VARCHAR(100),
        Phone VARCHAR(15),
        Region VARCHAR(100),
        Correspondent BOOLEAN
    );
    ''')


    # Add other tables similarly...

    conn.commit()
    cursor.close()
    conn.close()

create_tables()

def add_banquet(guest_id, date, time, table, guest_num, menu):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Banquet (GuestID, Date, Time, Table, Guest_num, Menu) VALUES (%s, %s, %s, %s, %s, %s)
    ''', (guest_id, date, time, table, guest_num, menu))
    conn.commit()
    cursor.close()
    conn.close()