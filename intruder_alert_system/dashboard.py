import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import ttk

# ---------------- FUNCTIONS ---------------- #

def start_camera():
    import detect

def intruder_detection():
    messagebox.showinfo("Detection", "Intruder Detection Active")

def weapon_detection():
    messagebox.showinfo("Weapon", "Weapon Detection Active")

def logout():
    window.destroy()

# View Logs Function
def view_logs():

    log_window = tk.Toplevel()
    log_window.title("Access Logs")
    log_window.geometry("700x400")
    log_window.config(bg="#2c3e50")

    title = tk.Label(
        log_window,
        text="Access Logs",
        font=("Arial", 20, "bold"),
        bg="#2c3e50",
        fg="white"
    )
    title.pack(pady=10)

    # Table
    tree = ttk.Treeview(
        log_window,
        columns=("Username", "Login Time"),
        show="headings"
    )

    tree.heading("Username", text="Username")
    tree.heading("Login Time", text="Login Time")

    tree.column("Username", width=200)
    tree.column("Login Time", width=400)

    tree.pack(fill="both", expand=True, padx=20, pady=20)

    # Database
    conn = sqlite3.connect("security_system.db")
    cursor = conn.cursor()

    cursor.execute("SELECT username, login_time FROM access_logs")

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()

# ---------------- MAIN WINDOW ---------------- #

window = tk.Tk()

window.title("Intruder Alert System")
window.geometry("600x550")
window.config(bg="#1e1e1e")

# Title
title = tk.Label(
    window,
    text="INTRUDER ALERT SYSTEM",
    font=("Arial", 24, "bold"),
    fg="#00ffcc",
    bg="#1e1e1e"
)
title.pack(pady=30)

# Subtitle
subtitle = tk.Label(
    window,
    text="AI Security Monitoring Dashboard",
    font=("Arial", 14),
    fg="white",
    bg="#1e1e1e"
)
subtitle.pack(pady=5)

# Buttons Style
button_style = {
    "font": ("Arial", 13, "bold"),
    "width": 25,
    "height": 2,
    "fg": "white",
    "bd": 0,
    "cursor": "hand2"
}

# Buttons
btn_camera = tk.Button(
    window,
    text="Start Camera",
    bg="#3498db",
    command=start_camera,
    **button_style
)
btn_camera.pack(pady=15)

btn_intruder = tk.Button(
    window,
    text="Intruder Detection",
    bg="#f39c12",
    command=intruder_detection,
    **button_style
)
btn_intruder.pack(pady=15)

btn_weapon = tk.Button(
    window,
    text="Weapon Detection",
    bg="#e74c3c",
    command=weapon_detection,
    **button_style
)
btn_weapon.pack(pady=15)

btn_logs = tk.Button(
    window,
    text="View Access Logs",
    bg="#2ecc71",
    command=view_logs,
    **button_style
)
btn_logs.pack(pady=15)

btn_logout = tk.Button(
    window,
    text="Logout",
    bg="#7f8c8d",
    command=logout,
    **button_style
)
btn_logout.pack(pady=25)

# Footer
footer = tk.Label(
    window,
    text="Developed using Python, OpenCV & YOLO",
    font=("Arial", 10),
    fg="gray",
    bg="#1e1e1e"
)
footer.pack(side="bottom", pady=10)

# Run
window.mainloop()