# import cv2
# from ultralytics import YOLO

# # Load the YOLOv8 model
# model = YOLO('yolov8n-pose.pt')

# # Open the video file
# # video_path = "peoplecount2.mp4"
# cap = cv2.VideoCapture(0)

# # Wiindow size
# size_fullhd = (1920,1080)
# size_hd = (1280,720)

# window_width = size_fullhd[0]
# window_height = size_fullhd[1]

# # Scaling factors
# scaling_factor_x = window_width / cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# scaling_factor_Y = window_height / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)


# # Loop through the video frames
# while cap.isOpened():
#     # Read a frame from the video
#     success, frame = cap.read()

#     # Resized the frame
#     resized_frame = cv2.resize(frame, (window_width, window_height))

#     if success:
#         # Run YOLOv8 inference on the frame
#         results = model(resized_frame)

#         # Visualize the results on the frame
#         resized_frame = results[0].plot()
        
#         # Display the annotated frame
#         cv2.imshow("YOLOv8 Inference", resized_frame)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         # Break the loop if the end of the video is reached
#         break

# # Release the video capture object and close the display window
# cap.release()
# cv2.destroyAllWindows()

# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.relase()
# cv2.destroyAllWindows()

import cv2

# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read a frame from the camera.")
            break

        # Display the frame (not recommended for headless)
        cv2.imshow('Webcam Feed', frame)

        # Check for a key press to exit
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' key to exit
            break

# Release the camera and close any OpenCV windows (not recommended for headless)
cap.release()
cv2.destroyAllWindows()
