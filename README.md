# Wabbajack Autoclicker

## Overview

This Python script is an autoclicker designed to facilitate the downloading of modpacks using Wabbajack without the need for a Nexus Mods Premium account. The script automates the process of finding and clicking the download button, saving you time and effort.

## Features

- Automatically searches for and clicks the Nexus Mods download button.
- Bypasses the need for a premium account when downloading modpacks with Wabbajack.
- Continuous operation until the user decides to stop the script.
- Adjustable image matching threshold for improved accuracy.

## Requirements

Make sure you have the following Python packages installed:

- `pyautogui`: For controlling the mouse and keyboard.
- `opencv-python`: For image processing and template matching.
- `numpy`: For handling arrays and image data.
- `keyboard`: For detecting keyboard inputs.

You can install the required packages using pip:

```python
pip install pyautogui opencv-python numpy keyboard
```

## Usage

1. **Prepare the Target Image**: Ensure that you have a screenshot of the Nexus Mods download button saved as `button.png` (or update the path in the code).

2. **Run the Script**: Execute the script using Python.

3. **Stop the Script**: To stop the script at any time, press `Ctrl + Q`.

## Code Explanation

### Main Functionality

- **`find_and_click(target_image)`**: This function takes the path to the target image, captures the current screen, and attempts to find and click the specified image.
  - Uses OpenCV’s `matchTemplate` method to locate the image.
  - Clicks on the center of the found image if the match exceeds a defined threshold.

- **`main()`**: The main loop of the script that continuously searches for the target image.
  - Calls `find_and_click` and waits 2 seconds before the next search.
  - Moves the mouse to a predetermined position after clicking.
  - Listens for the `Ctrl + Q` hotkey to exit the loop.


## Configuration

- **Image Path**: Change the `target_image_path` variable in the `main()` function to point to your desired image file if it's named differently.
- **Matching Threshold**: Adjust the `threshold` variable within the `find_and_click` function to change how strictly the script looks for the target image (default is 0.8).

## Notes

- Ensure that the target image (Nexus Mods download button) is visible on the screen and is not occluded by other windows for successful detection.
- The script requires sufficient screen resolution and may not perform well on very low-resolution displays.

## License

This project is open-source and available under the MIT License.
