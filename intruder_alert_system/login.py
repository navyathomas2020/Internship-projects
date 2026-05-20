import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function for login
def login_user():
    username = entry_username.get()
    password = entry_password.get()

    # Connect database
    conn = sqlite3.connect("security_system.db")
    cursor = conn.cursor()

    # Check username and password
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    if user:
        # Save login time
        cursor.execute(
            "INSERT INTO access_logs (username) VALUES (?)",
            (username,)
        )

        conn.commit()

        messagebox.showinfo("Success", "Login Successful")
        window.destroy()
        import dashboard
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

    conn.close()


# Main window
window = tk.Tk()
window.title("Intruder Alert System - Login")
window.geometry("400x300")
window.config(bg="lightgreen")

# Title
title = tk.Label(
    window,
    text="User Login",
    font=("Arial", 18, "bold"),
    bg="lightgreen"
)
title.pack(pady=20)

# Username
label_username = tk.Label(window, text="Username", bg="lightgreen")
label_username.pack()

entry_username = tk.Entry(window, width=30)
entry_username.pack(pady=5)

# Password
label_password = tk.Label(window, text="Password", bg="lightgreen")
label_password.pack()

entry_password = tk.Entry(window, width=30, show="*")
entry_password.pack(pady=5)

# Login Button
btn_login = tk.Button(
    window,
    text="Login",
    bg="blue",
    fg="white",
    width=15,
    command=login_user
)
btn_login.pack(pady=20)

# Run window
window.mainloop()