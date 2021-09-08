from PIL import Image
import pytesseract
cv2 = "cv2"
import cv2
from googletrans import Translator
import plyer
import pyautogui
from pynput import mouse
import numpy 
import keyboard
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import time
import requests



# pytesseract.pytesseract.tesseract_cmd = '‪C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
x_, y_ = 0, 0
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
token = "118aa051d3c711a28d1531bd841f344c7acd582e5dbb8fbadda613ab19dec491e2d4a22e788727c61531f"
vk = vk_api.VkApi(token=token)
fruha_vk = '210437700'


def get_text_from_picture(pil_image):
    img_rgb = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)

    translator = Translator()

    text_en = pytesseract.image_to_string(img_rgb).replace('\n', ' ')

    return (text_en)

def get_translation(text_en):
    translator = Translator()
    text_ru = translator.translate(text_en, dest='ru').text

    print("ru: ", text_ru)
    print("en: ", text_en)

    return (text_ru)


def throw_notification(message):
    message = message[:min(256, len(message))]
    plyer.notification.notify(message=message,
                            #   app_name='qwerty',
                              timeout=10,
                            #   app_icon='icon1.png',
                              )

def get_two_points():
    def on_click(x, y, button, pressed):
        global x_, y_
        x_, y_ = x, y
        if (button == mouse.Button.left) and (pressed == True):
            print(button)
            return False
        else:
            pass
    points = []
    for i in range(2):
        listener = mouse.Listener(on_click=on_click)
        listener.start()
        listener.join()
        points.append([x_, y_])
    p1 = points[0].copy()
    p2 = points[1].copy()
    points[0][0] = min(p1[0], p2[0])
    points[0][1] = min(p1[1], p2[1])
    points[1][0] = max(p1[0], p2[0])
    points[1][1] = max(p1[1], p2[1])
    return points


def create_screenshot():
    screenshot = pyautogui.screenshot()
    points = get_two_points()
    print(points)
    cropped_img = screenshot.crop((points[0][0], points[0][1], points[1][0], points[1][1]))
    # cropped_img.show()
    return cropped_img

def write_msg_vk(user_id, message):
    try:
        vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(1,10000000000)})
    except:
        print('vk_error')
        
def get_summary(text_title):
    # text_title = text_title.replace('.', ' ')
    # text_title = text_title.replace('?', '.')
    text_title = text_title.strip(' \n')
    # text_title = ''.join(i for i in text_title if not i.isdigit())
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': text_title,
        },
        headers={'api-key': 'f9a98697-9629-4375-af1d-0045585bbab5'}
    )

    text_summary = r.json()['output']
    print("text_title: ", text_title,'1')
    print("text_summary: ", text_summary)
    return text_summary

def translate(inp):
    print('ctrl + shift + z Detected')
    pil_image = create_screenshot()
    text_en = get_text_from_picture(pil_image)
    text_ru = get_translation(text_en)
    if (inp == '1'):
        throw_notification(text_ru)
    if (inp == '2'):
        write_msg_vk(fruha_vk, text_ru)

def summary(inp):
    print('ctrl + shift + x Detected')
    pil_image = create_screenshot()
    text_title = get_text_from_picture(pil_image)
    text_summary = get_summary(text_title)
    if (inp == '1'):
        throw_notification(text_summary)
    if (inp == '2'):
        write_msg_vk(fruha_vk, text_summary)

if __name__ == "__main__":
    print('Start')
    print('1: Windows notifications')
    print('2: Vk messages')
    print('ctrl + shift + z to translate')
    print('ctrl + shift + x to get summary')
    inp = input()

    keyboard.add_hotkey('ctrl + shift + z', translate, args=(inp))
    keyboard.add_hotkey('ctrl + shift + x', summary, args=(inp))
    keyboard.wait('esc')
    print('End')

