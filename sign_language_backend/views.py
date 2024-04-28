import cv2
import numpy as np
from keras.models import model_from_json
from function import mediapipe_detection, extract_keypoints

def detect_gesture(request):
    # Load the trained model and other required variables
    json_file = open("model.json", "r")
    model_json = json_file.read()
    json_file.close()
    model = model_from_json(model_json)
    model.load_weights("model.h5")
    actions = [...]  # List of gesture actions (e.g., ['gesture_1', 'gesture_2', ...])

    # Set up OpenCV video capture
    cap = cv2.VideoCapture(0)  # Use webcam (change the argument for other video sources)

    # Initialize variables for gesture detection
    sequence = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        crop_frame = frame[40:400, 0:300]  # Crop the frame if needed
        image = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for compatibility with model

        # Make detections
        keypoints = extract_keypoints(...)  # Define how to extract keypoints from mediapipe results
        sequence.append(keypoints)
        sequence = sequence[-30:]

        if len(sequence) == 30:
            sequence_array = np.expand_dims(sequence, axis=0)
            res = model.predict(sequence_array)[0]
            predicted_action = actions[np.argmax(res)]

            # Perform further logic with predicted_action (e.g., formulating sentences)

            # Display output on the frame
            cv2.putText(frame, f"Detected Action: {predicted_action}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Convert the frame to JPEG format for streaming to frontend (optional)
        _, jpeg_frame = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg_frame.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
