This project demonstrates real-time object detection using the YOLOv8 model from Ultralytics with OpenCV and a webcam. The model detects multiple objects in a live video stream and draws bounding boxes with labels and confidence scores.

📸 Demo
<!-- Replace with your own screenshot or remove this section -->

📂 Features
✅ Real-time object detection from webcam

✅ Automatically downloads YOLOv8n model if not found

✅ Displays detected objects with labels and confidence scores

✅ Save detection frame with s key

✅ Quit with q key

🔧 Requirements
Make sure you have the following installed:

Python 3.8+

Ultralytics YOLO

OpenCV

Torch

📦 Install dependencies
bash
Copy
Edit
pip install ultralytics opencv-python torch
▶️ Run the Project
bash
Copy
Edit
python object_detection.py
Once the script is running:

Press s to save the current frame as an image (detected_objects.jpg)

Press q to quit the webcam feed

📁 File Structure
bash
Copy
Edit
.
├── object_detection.py      # Main detection script
├── yolov8n.pt               # YOLOv8n model (auto-downloaded if not present)
├── detected_objects.jpg     # Saved image from detection (when 's' is pressed)
└── README.md                # Project documentation
🙌 Acknowledgements
Ultralytics for the YOLOv8 model

OpenCV for video capture and visualization

📃 License
This project is licensed under the MIT License. Feel free to use and modify it!

