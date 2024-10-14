import cv2
import os
import time

# Function to capture a frame, resize it, and save as an image file
def capture_and_save_frame(cap, filename='frame.jpg', new_width=100):
    ret, frame = cap.read()

    if not ret or frame is None:
        print("Failed to capture frame.")
        return False

    # Resize the frame
    height, width = frame.shape[:2]
    ratio = new_width / width
    new_height = int(height * ratio)
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # Save the frame as an image file
    cv2.imwrite(filename, resized_frame)
    return True

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)

try:
    while True:
        if capture_and_save_frame(cap):
            # Clear the terminal
            os.system('clear')  # Use 'cls' on Windows

            # Use jp2a to convert the image to ASCII and print it in the terminal
            os.system('jp2a --width=100 --height=30 frame.jpg')

        # Introduce a delay of 0.005 seconds
        time.sleep(0.00005)

        # Add a break condition
 #      if cv2.waitKey(1) & 0xFF == ord('q'):
  #        break

finally:
    # Clean up
    cap.release()
    cv2.destroyAllWindows()
    if os.path.exists('frame.jpg'):
        os.remove('frame.jpg')
