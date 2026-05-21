import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# Vehicle classes
vehicle_classes = ["car", "motorcycle", "bus", "truck"]

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Vehicle counter
    vehicle_count = 0

    # Run YOLO detection
    results = model(frame)

    # Process detections
    for result in results:
        boxes = result.boxes

        for box in boxes:

            # Get class ID
            cls = int(box.cls[0])

            # Get class name
            class_name = model.names[cls]

            # Detect only vehicles
            if class_name in vehicle_classes:

                # Increase count
                vehicle_count += 1

                # Bounding box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw rectangle
                cv2.rectangle(frame,
                              (x1, y1),
                              (x2, y2),
                              (0, 255, 0),
                              2)

                # Vehicle label
                cv2.putText(frame,
                            class_name,
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 255, 0),
                            2)

    # Traffic Density Analysis
    if vehicle_count <= 5:
        traffic_status = "LOW TRAFFIC"

    elif vehicle_count <= 10:
        traffic_status = "MEDIUM TRAFFIC"

    else:
        traffic_status = "HIGH TRAFFIC"

    # Display vehicle count
    cv2.putText(frame,
                f"Vehicle Count: {vehicle_count}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3)

    # Display traffic status
    cv2.putText(frame,
                f"Traffic Status: {traffic_status}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                3)

    # Show output
    cv2.imshow("Smart Traffic Monitoring System", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()