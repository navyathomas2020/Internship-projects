import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to register user
def register_user():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    # Connect database
    conn = sqlite3.connect("security_system.db")
    cursor = conn.cursor()

    # Insert user data
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Registration Successful")

    # Clear fields
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)


# Main window
window = tk.Tk()
window.title("Intruder Alert System - Register")
window.geometry("400x300")
window.config(bg="lightblue")

# Title
title = tk.Label(
    window,
    text="User Registration",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title.pack(pady=20)

# Username
label_username = tk.Label(window, text="Username", bg="lightblue")
label_username.pack()

entry_username = tk.Entry(window, width=30)
entry_username.pack(pady=5)

# Password
label_password = tk.Label(window, text="Password", bg="lightblue")
label_password.pack()

entry_password = tk.Entry(window, width=30, show="*")
entry_password.pack(pady=5)

# Register Button
btn_register = tk.Button(
    window,
    text="Register",
    bg="green",
    fg="white",
    width=15,
    command=register_user
)
btn_register.pack(pady=20)

# Run window
window.mainloop()