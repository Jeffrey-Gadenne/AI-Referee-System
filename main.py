# AI Referee System - Main Entry Point

import cv2
import mediapipe as mp
import time
from datetime import datetime

print("🚀 AI Referee System Starting...")
print("Camera feed + Pose Detection Active")
print("Press 'q' to quit\n")

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Process frame
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = pose.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ Player pose detected - Analyzing behavior...")

    cv2.imshow('AI Referee - Live Detection', image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ System shutdown cleanly. Good job!")