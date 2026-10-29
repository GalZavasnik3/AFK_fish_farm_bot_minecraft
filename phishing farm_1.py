import pyautogui
import cv2
import numpy as np
import time

# Nastavitve
IMAGE_PATH = "fishing_bobber.png"
CONFIDENCE = 0.8      # znižaj na 0.7 če ne zazna
CHECK_DELAY = 0.5     # hitrost preverjanja

# Naloži sliko
template = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
h, w = template.shape

screen_width, screen_height = pyautogui.size()

# Definiraj desni spodnji kot (zadnja četrtina zaslona)
region = (
    int(screen_width * 0.6),
    int(screen_height * 0.6),
    int(screen_width * 0.4),
    int(screen_height * 0.4),
)


while True:
    screenshot = pyautogui.screenshot(region=region)
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= CONFIDENCE:
        click_x = region[0] + max_loc[0] + w // 2
        click_y = region[1] + max_loc[1] + h // 2 

        pyautogui.rightClick(click_x, click_y)
       
        time.sleep(1)  # da ne klika večkrat zapored

    time.sleep(CHECK_DELAY)
