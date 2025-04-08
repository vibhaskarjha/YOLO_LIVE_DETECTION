import os
import urllib.request
import cv2
import torch
from ultralytics import YOLO

# ✅ Auto-download YOLOv8n model if not found locally
model_path = "yolov8n.pt"
model_url = "https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov8n.pt"

if not os.path.exists(model_path):
    print("⬇️ Downloading YOLOv8n model...")
    urllib.request.urlretrieve(model_url, model_path)
    print("✅ Download complete!")

# ✅ Load the YOLOv8 model
model = YOLO(model_path)

# ✅ Initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # ✅ Perform object detection
    results = model(frame)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])        # Bounding box coordinates
            confidence = float(box.conf[0])               # Confidence score
            class_id = int(box.cls[0])                    # Class ID
            label = result.names[class_id]                # Object class label

            # ✅ Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # ✅ Display label and confidence
            text = f"{label}: {confidence:.2f}"
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.7, (0, 255, 0), 2)

    # ✅ Show output frame
    cv2.imshow("Object Detector (YOLOv8)", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite("detected_objects.jpg", frame)
        print("📸 Image saved!")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
