import streamlit as st
import sqlite3
import cv2
from ultralytics import YOLO
from datetime import datetime
import os

# ---------------- CREATE SCREENSHOT FOLDER ---------------- #

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# ---------------- LOAD YOLO MODEL ---------------- #

model = YOLO("yolov8n.pt")

# ---------------- DATABASE ---------------- #

conn = sqlite3.connect("security_system.db", check_same_thread=False)
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# Create access logs table
cursor.execute("""
CREATE TABLE IF NOT EXISTS access_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Intruder Alert System",
    layout="wide"
)

# ---------------- TITLE ---------------- #

st.title("🔐 Intruder Alert System")
st.markdown("### AI-Based Security Monitoring Using YOLO")

# ---------------- SIDEBAR MENU ---------------- #

menu = st.sidebar.selectbox(
    "Select Option",
    ["Register", "Login", "Detection", "View Logs"]
)

# ==========================================================
# REGISTER
# ==========================================================

if menu == "Register":

    st.subheader("User Registration")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Register"):

        if new_user == "" or new_pass == "":
            st.error("Please fill all fields")

        else:

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (new_user, new_pass)
            )

            conn.commit()

            st.success("Registration Successful")

# ==========================================================
# LOGIN
# ==========================================================

elif menu == "Login":

    st.subheader("User Login")

    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    if st.button("Login"):

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        if user:

            cursor.execute(
                "INSERT INTO access_logs (username) VALUES (?)",
                (username,)
            )

            conn.commit()

            st.success("Login Successful")

        else:
            st.error("Invalid Username or Password")

# ==========================================================
# DETECTION
# ==========================================================

elif menu == "Detection":

    st.subheader("AI Intruder & Weapon Detection")

    run = st.checkbox("Start Camera")

    FRAME_WINDOW = st.image([])

    cap = cv2.VideoCapture(0)

    while run:

        ret, frame = cap.read()

        if not ret:
            st.error("Failed to access camera")
            break

        # YOLO Detection
        results = model(frame)

        weapon_detected = False

        for result in results:

            boxes = result.boxes

            for box in boxes:

                class_id = int(box.cls[0])

                class_name = model.names[class_id]

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # ---------------- PERSON DETECTION ---------------- #

                if class_name == "person":

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    cv2.putText(
                        frame,
                        "Person Detected",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2
                    )

                # ---------------- WEAPON DETECTION ---------------- #

                if class_name in ["knife", "scissors"]:

                    weapon_detected = True

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 0, 255),
                        3
                    )

                    cv2.putText(
                        frame,
                        "WEAPON DETECTED!",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        2
                    )

        # ---------------- ALERT SYSTEM ---------------- #

        if weapon_detected:

            cv2.putText(
                frame,
                "DANGER ALERT!",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

            st.warning("⚠ Weapon Detected!")

            # Save Screenshot
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            filename = f"screenshots/alert_{timestamp}.jpg"

            cv2.imwrite(filename, frame)

        # Convert frame BGR → RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Show frame
        FRAME_WINDOW.image(frame)

    # Release camera properly
    cap.release()

# ==========================================================
# VIEW LOGS
# ==========================================================

elif menu == "View Logs":

    st.subheader("Access Logs")

    cursor.execute(
        "SELECT username, login_time FROM access_logs"
    )

    rows = cursor.fetchall()

    st.table(rows)