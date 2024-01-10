
import pyautogui


def perform_click(command):
    if command == "esquerdo":
        pyautogui.click(button='left')
    elif command == "direito":
        pyautogui.click(button='right')
    elif command == "segurar":
        pyautogui.mouseDown(button='left')
    elif command == "soltar":
        pyautogui.mouseUp(button='left')
