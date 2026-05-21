import streamlit as st
import cv2
from ultralytics import YOLO
import numpy as np

# Page title
st.title("Smart Traffic Monitoring System")

# Load YOLO model
model = YOLO("yolov8n.pt")

# Vehicle classes
vehicle_classes = ["car", "motorcycle", "bus", "truck"]

# Start button
start = st.button("Start Monitoring")

# Stop button
stop = st.button("Stop")

# Placeholder for video
frame_placeholder = st.empty()

# Traffic info placeholder
info_placeholder = st.empty()

# Webcam
cap = cv2.VideoCapture(0)

# Control variable
run = start

while run:

    ret, frame = cap.read()

    if not ret:
        st.error("Cannot access webcam")
        break

    # Vehicle count
    vehicle_count = 0

    # YOLO detection
    results = model(frame)

    for result in results:
        boxes = result.boxes

        for box in boxes:

            cls = int(box.cls[0])
            class_name = model.names[cls]

            if class_name in vehicle_classes:

                vehicle_count += 1

                # Bounding box
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame,
                              (x1, y1),
                              (x2, y2),
                              (0, 255, 0),
                              2)

                # Label
                cv2.putText(frame,
                            class_name,
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 255, 0),
                            2)

    # Traffic analysis
    if vehicle_count <= 5:
        traffic_status = "LOW TRAFFIC"

    elif vehicle_count <= 10:
        traffic_status = "MEDIUM TRAFFIC"

    else:
        traffic_status = "HIGH TRAFFIC"

    # Display count on frame
    cv2.putText(frame,
                f"Vehicle Count: {vehicle_count}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3)

    # Display traffic status
    cv2.putText(frame,
                f"Traffic: {traffic_status}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                3)

    # Convert BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Show video in Streamlit
    frame_placeholder.image(frame,
                            channels="RGB")

    # Show information
    info_placeholder.write(f"""
    ### Traffic Information
    - Vehicle Count: {vehicle_count}
    - Traffic Status: {traffic_status}
    """)

    # Stop button
    if stop:
        run = False

cap.release()