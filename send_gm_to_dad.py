import pywhatkit as kit
import schedule
import time
import pytz
import random
import pyautogui
from datetime import datetime

#Set number
dad_number = "+919705599839"

#Message list
messages = [
    "Hello!",
    "Hi!",
    "Hey!"
]

def send_good_morning():
    message = random.choice(messages)

    #Get current time in IST
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)

    print(f"[{now.strftime('%Y-%m-%d %H-%M-%S')}] Sending message: '{message}'")

    kit.sendwhatmsg_instantly(dad_number, message, wait_time=30, tab_close=True)
    time.sleep(10)
    pyautogui.press("enter")

    print('Message Sent!')

send_good_morning()