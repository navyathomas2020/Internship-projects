import cv2
from ultralytics import YOLO
import os
from datetime import datetime

# Load YOLO model
model = YOLO("yolov8n.pt")

# Create screenshots folder if not exists
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access camera")
    exit()

print("Weapon Detection System Started")

# Start loop
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run detection
    results = model(frame)

    # Detection flag
    weapon_detected = False

    for result in results:
        boxes = result.boxes

        for box in boxes:
            class_id = int(box.cls[0])

            class_name = model.names[class_id]

            # Get coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # PERSON DETECTION
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

            # WEAPON DETECTION
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

    # ALERT MESSAGE
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

        # Save screenshot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"screenshots/alert_{timestamp}.jpg"

        cv2.imwrite(filename, frame)

    # Show frame
    cv2.imshow("Intruder & Weapon Detection System", frame)

    # Exit on Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release
cap.release()
cv2.destroyAllWindows()