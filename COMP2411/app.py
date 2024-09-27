import psycopg2
import tkinter as tk
from tkinter import messagebox, simpledialog

# Database setup
def init_db():
    conn = psycopg2.connect(
        dbname='bonquet', 
        user='postgres',   
        password='baizhu0901', 
        host='localhost',        
        port='5432'              
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bonquets (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Functions to interact with the database
def add_bonquet(title, author):
    conn = psycopg2.connect(
        dbname='bonquet', 
        user='postgres',   
        password='baizhu0901', 
        host='localhost',        
        port='5432'     
    )
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bonquets (title, author) VALUES (%s, %s)', (title, author))
    conn.commit()
    cursor.close()
    conn.close()

def delete_bonquet(bonquet_id):
    conn = psycopg2.connect(
        dbname='bonquet', 
        user='postgres',   
        password='baizhu0901', 
        host='localhost',        
        port='5432'     
    )
    cursor = conn.cursor()
    cursor.execute('DELETE FROM bonquets WHERE id = %s', (bonquet_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_bonquets():
    conn = psycopg2.connect(
        dbname='bonquet', 
        user='postgres',   
        password='baizhu0901', 
        host='localhost',        
        port='5432'     
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bonquets')
    bonquets = cursor.fetchall()
    cursor.close()
    conn.close()
    return bonquets

# GUI Application
class bonquetManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("bonquet Management System")

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add bonquet", command=self.add_bonquet)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete bonquet", command=self.delete_bonquet)
        self.delete_button.pack(pady=5)

        self.load_bonquets()

    def load_bonquets(self):
        self.listbox.delete(0, tk.END)
        bonquets = get_bonquets()
        for bonquet in bonquets:
            self.listbox.insert(tk.END, f"{bonquet[1]} by {bonquet[2]} (ID: {bonquet[0]})")

    def add_bonquet(self):
        title = simpledialog.askstring("Input", "Enter bonquet title:")
        author = simpledialog.askstring("Input", "Enter author name:")
        if title and author:
            add_bonquet(title, author)
            self.load_bonquets()
        else:
            messagebox.showwarning("Input Error", "Please enter both title and author.")

    def delete_bonquet(self):
        selected = self.listbox.curselection()
        if selected:
            bonquet_id = self.listbox.get(selected[0]).split("(ID: ")[1][:-1]
            delete_bonquet(bonquet_id)
            self.load_bonquets()
        else:
            messagebox.showwarning("Selection Error", "Please select a bonquet to delete.")

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = bonquetManagementApp(root)
    root.mainloop()