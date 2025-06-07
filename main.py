import tkinter as tk
from tkinter import messagebox
import sqlite3
from cryptography.fernet import Fernet

# Paste your key here
key = b'eWGyGb-A6UwlofJMqOlyXwojRlPksj1VWR031FLtvWU='
fernet = Fernet(key)

# Connect to SQLite database
conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY,
    website TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

# Save password
def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if not (website and username and password):
        messagebox.showerror("Error", "All fields are required!")
        return

    encrypted_pass = fernet.encrypt(password.encode())
    cursor.execute("INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
                   (website, username, encrypted_pass))
    conn.commit()
    messagebox.showinfo("Saved", "Password saved successfully!")

# View all
def view_passwords():
    cursor.execute("SELECT website, username, password FROM passwords")
    rows = cursor.fetchall()
    display.delete(1.0, tk.END)
    for row in rows:
        decrypted_pass = fernet.decrypt(row[2]).decode()
        display.insert(tk.END, f"Website: {row[0]}\nUsername: {row[1]}\nPassword: {decrypted_pass}\n\n")

# Search by website
def search_password(website):
    cursor.execute("SELECT website, username, password FROM passwords WHERE website = ?", (website,))
    rows = cursor.fetchall()
    display.delete(1.0, tk.END)
    if not rows:
        display.insert(tk.END, "No entry found.\n")
    for row in rows:
        decrypted_pass = fernet.decrypt(row[2]).decode()
        display.insert(tk.END, f"Website: {row[0]}\nUsername: {row[1]}\nPassword: {decrypted_pass}\n\n")

# Delete by website
def delete_password(website):
    cursor.execute("SELECT * FROM passwords WHERE website = ?", (website,))
    if cursor.fetchone() is None:
        messagebox.showinfo("Not Found", "No entry found for this website.")
        return
    confirm = messagebox.askyesno("Delete", f"Delete all entries for '{website}'?")
    if confirm:
        cursor.execute("DELETE FROM passwords WHERE website = ?", (website,))
        conn.commit()
        display.delete(1.0, tk.END)
        messagebox.showinfo("Deleted", "Password(s) deleted.")

# GUI
app = tk.Tk()
app.title("Password Manager")

tk.Label(app, text="Website:").grid(row=0, column=0)
tk.Label(app, text="Username:").grid(row=1, column=0)
tk.Label(app, text="Password:").grid(row=2, column=0)

entry_website = tk.Entry(app, width=30)
entry_username = tk.Entry(app, width=30)
entry_password = tk.Entry(app, width=30, show="*")

entry_website.grid(row=0, column=1)
entry_username.grid(row=1, column=1)
entry_password.grid(row=2, column=1)

tk.Button(app, text="Save", command=save_password).grid(row=3, column=0, pady=5)
tk.Button(app, text="View All", command=view_passwords).grid(row=3, column=1, pady=5)

tk.Label(app, text="Search/Delete Website:").grid(row=4, column=0)
entry_search = tk.Entry(app, width=30)
entry_search.grid(row=4, column=1)

tk.Button(app, text="Search", command=lambda: search_password(entry_search.get())).grid(row=5, column=0)
tk.Button(app, text="Delete", command=lambda: delete_password(entry_search.get())).grid(row=5, column=1)

display = tk.Text(app, height=10, width=50)
display.grid(row=6, column=0, columnspan=2, pady=10)

app.mainloop()



