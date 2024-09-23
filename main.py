import pyautogui
import cv2
import numpy as np
import time
import keyboard

# Function to search for an image on the screen and click on it
def find_and_click(target_image):
    # Capture the screen
    screenshot = pyautogui.screenshot()
    
    # Convert the screenshot to a format that OpenCV can use
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Load the target image (the button or item you're looking for)
    template = cv2.imread(target_image)

    # Perform template matching using matchTemplate function
    result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Define a matching threshold
    threshold = 0.8  # Adjust this value as needed

    # If the match is greater than the threshold, perform a click
    if max_val >= threshold:
        # Get the coordinates of the center of the found image
        click_x = max_loc[0] + template.shape[1] // 2
        click_y = max_loc[1] + template.shape[0] // 2
        
        # Move the mouse and click at the position
        pyautogui.moveTo(click_x, click_y, duration=0.5)
        pyautogui.click()
        print(f'Image found and clicked at: ({click_x}, {click_y})')
        return True
    else:
        print('Image not found on screen.')
        return False


def main():
    # Path to the target image (e.g., 'button.png')
    target_image_path = 'button.png'

    # Constant retry until the image is found
    while True:
        if find_and_click(target_image_path):
            time.sleep(2)  # Wait 2 seconds before searching again
            pyautogui.moveTo(100, 100)  # Move mouse to a specific position

        # Break the loop if "ctrl+q" is pressed
        if keyboard.is_pressed("ctrl+q"):
            break


# Fix the condition for running the script directly
if __name__ == "__main__":
    main()
