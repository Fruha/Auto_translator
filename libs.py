import os

libs = [
    "pytesseract",
    "opencv-python",
    "googletrans==3.1.0a0",
    "plyer",
    "pyautogui",
    "pynput",
    "keyboard",
    "vk_api",
    
    ]

for lib in libs:
    os.system(f"pip install {lib}")

