"""
On GitHub Repo: https://github.com/CoronaKlledMe/piano-tiles-bot
"""

# For taking screenshots
from mss import mss

# For mouse controls
import pyautogui

# For terminating infinite loop
import keyboard

"""
Getting Mouse Positions (In terminal)
"""

# Starting position
x_start, y_start = 229, 529

# Ending position
x_end, y_end = 601, 609

# Look for this color
target_color = (0,) # 0 = Black


def main():
    screenshot_coordinate = (
        x_start, y_start,
        x_end, y_end
    )

    columns = int(
        (x_end - x_start) / 4 # Since it has four columns
    )

    tile = int(columns/2)

    mid_tiles = (
        tile, # First column
        tile + columns, # Second column
        tile + columns*2, # Third column
        tile + columns*3, # Fourth column
    )

    with mss() as screenshot:
        image = screenshot.grab(screenshot_coordinate)

        # Checking for all tiles in that screenshot
        for mid_tile in mid_tiles:

            # Checking for black tile
            if image.pixel(mid_tile, 0)[0] in target_color:

                # Positioning mouse under that tile and clicking it
                pyautogui.click(
                    x_start + mid_tile,
                    y_end
                )


# Increasing mouse clicking speed
pyautogui.PAUSE = 0.0001 # Decrease the value to increase speed


print("Press 'e' to exit.")

# Running main function infinite times
while True:
    if keyboard.is_pressed('e'):
        print("You have pressed 'e'. Bot exited.")
        break
    
    else:
        main()

