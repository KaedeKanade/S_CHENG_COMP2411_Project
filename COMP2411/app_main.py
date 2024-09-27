import tkinter as tk
from tkinter import messagebox
from db_functions import create_connection

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Management System")

        # Sign Up
        self.signup_frame = tk.Frame(self.root)
        self.signup_frame.pack()

        tk.Label(self.signup_frame, text="First Name").grid(row=0, column=0)
        self.first_name_entry = tk.Entry(self.signup_frame)
        self.first_name_entry.grid(row=0, column=1)

        tk.Label(self.signup_frame, text="Last Name").grid(row=1, column=0)
        self.last_name_entry = tk.Entry(self.signup_frame)
        self.last_name_entry.grid(row=1, column=1)

        tk.Button(self.signup_frame, text="Sign Up", command=self.sign_up).grid(row=2, columnspan=2)

        # Sign In
        self.signin_frame = tk.Frame(self.root)
        self.signin_frame.pack()

        tk.Label(self.signin_frame, text="Email").grid(row=0, column=0)
        self.email_entry = tk.Entry(self.signin_frame)
        self.email_entry.grid(row=0, column=1)

        tk.Button(self.signin_frame, text="Sign In", command=self.sign_in).grid(row=1, columnspan=2)

    def create_connection():
        return create_connection()

    def sign_up(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Guest (FirstName, LastName, Email) VALUES (%s, %s, %s)
        ''', (self.first_name_entry.get(), self.last_name_entry.get(), self.email_entry.get()))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Sign Up Successful!")

    def sign_in(self):
        conn = self.create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM Guest WHERE Email = %s
        ''', (self.email_entry.get(),))
        guest = cursor.fetchone()
        cursor.close()
        conn.close()
        if guest:
            messagebox.showinfo("Success", f"Welcome {guest[1]} {guest[2]}!")
        else:
            messagebox.showerror("Error", "Invalid Email!")

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()