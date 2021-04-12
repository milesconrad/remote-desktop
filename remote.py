from pickle import loads
import socket

from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
from pynput.keyboard._win32 import KeyCode

downKeys = []
downButtons = []
client = socket.socket()
client.connect(('67.149.113.14', 600))
print('Connected!')

while True:
    client.send('confirmed'.encode())
    data = client.recv(1024)
    data = loads(data)
    
    if isinstance(data, list):
        x, y = data
        mouse.position = (x, y)

    elif isinstance(data, Button):
        if data not in downButtons:
            downButtons.append(data)
            mouse.press(data)
        else:
            downButtons.remove(data)
            mouse.release(data)
            
    elif isinstance(data, int):
        mouse.scroll(0, data)
    
    elif isinstance(data, Key) or isinstance(data, KeyCode):
        if data not in downKeys:
            downKeys.append(data)
            keyboard.press(data)
        else:
            downKeys.remove(data)
            keyboard.release(data)

client.close()
