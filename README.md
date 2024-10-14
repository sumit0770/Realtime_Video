Real-Time ASCII Facecam in Terminal

This project uses Python and OpenCV to capture a live webcam feed, convert each frame into an ASCII representation, and display it in the terminal using jp2a. The output refreshes in real-time, providing a unique way to visualize a facecam in ASCII art.
How It Works

    The script captures frames from the webcam using OpenCV.
    Each frame is resized and saved as an image file.
    The saved image is then converted to ASCII art using jp2a, which is displayed directly in the terminal.
    The process repeats in a loop to create a real-time effect.

Prerequisites

Make sure the following are installed on your system:

    Python 3.x
    OpenCV for capturing webcam frames:

    bash

pip install opencv-python

jp2a for converting images to ASCII:
(you can also use 'img2txt' command )

bash

    sudo apt-get install jp2a

Installation

    Clone the repository:

    bash

    Install dependencies: Install the required Python and system dependencies as mentioned above.

Running the Script

To start the real-time ASCII facecam, run:

bash

python terminal_facecam.py

Keyboard Controls

    Press 'q' to exit the script gracefully.

Customization

You can easily modify the script to change various settings:

    Frame Width: Adjust the new_width parameter in the capture_and_save_frame function to change the ASCII output width.
    Frame Rate: Use a delay (e.g., time.sleep(0.05)) in the loop for smoother or slower updates.
    Terminal Clear Command: Modify the os.system('clear') to os.system('cls') if running on Windows.

Example Output

Here’s what the ASCII output might look like in your terminal:

scss

          _____
         /     \
        | () () |
         \  ^  /
          |||||
          |||||

Troubleshooting

    Failed to capture frame: Ensure the webcam is connected and accessible.
    jp2a not found: Make sure jp2a is installed and added to the system path.

Limitations

    The script may not run smoothly on lower-spec systems due to the real-time nature of capturing and processing frames.
    Frame rate might be affected by terminal rendering capabilities.
