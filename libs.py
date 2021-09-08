import os

libs = [
    "pytesseract",
    "opencv-python",
    "googletrans",
    "plyer",
    "pyautogui",
    "pynput",
    "keyboard",
    "vk_api",
    
    ]

for lib in libs:
    os.system(f"pip install {lib}")

