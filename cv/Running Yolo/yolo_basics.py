from ultralytics import YOLO
import cv2

model = YOLO('C:/Users/SOMANATH/Desktop/cv/Yolo-Weights/yolov8l.pt')
results = model("C:/Users/SOMANATH/Desktop/cv/Running Yolo/Images/3.jpg", show = True)
cv2.waitKey(0)