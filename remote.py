from pickle import loads
import socket

from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
from pynput.keyboard._win32 import KeyCode

pressed_keys = []
pressed_buttons = []
client = socket.socket()
client.connect(('insert public IP address here', 600))
print('Connected!')

while True:
    client.send('confirmed'.encode())
    data = client.recv(1024)
    data = loads(data)
    
    if isinstance(data, list):
        x, y = data
        mouse.position = (x, y)

    # pynput has listeners for both mouseup and mousedown, so pressed_buttons keeps
    # track of which buttons are still being pressed
    elif isinstance(data, Button):
        if data not in pressed_buttons:
            pressed_buttons.append(data)
            mouse.press(data)
        else:
            pressed_buttons.remove(data)
            mouse.release(data)
            
    elif isinstance(data, int):
        mouse.scroll(0, data)
    
    # pynput has listeners for keyup and mousedown as well, so pressed_keys keeps
    # track of which keys are still being pressed
    elif isinstance(data, Key) or isinstance(data, KeyCode):
        if data not in pressed_keys:
            pressed_keys.append(data)
            keyboard.press(data)
        else:
            pressed_keys.remove(data)
            keyboard.release(data)

client.close()