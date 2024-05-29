import cv2
import time

def capture_photos(interval=10, output_folder="captured_photos"):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)
    
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        # Create the output folder if it doesn't exist
        import os
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        print("Starting photo capture. Press 'q' to quit.")
        
        # Start capturing images at intervals
        start_time = time.time()
        photo_count = 0
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture image.")
                break

            # Get the current time and calculate if the interval has passed
            current_time = time.time()
            if current_time - start_time >= interval:
                # Save the captured image
                photo_name = f"{output_folder}/photo_{photo_count}.jpg"
                cv2.imwrite(photo_name, frame)
                print(f"Captured {photo_name}")
                
                photo_count += 1
                start_time = current_time

            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press 'q' on keyboard to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

# Example usage: capture a photo every 10 seconds
capture_photos(interval=10)
