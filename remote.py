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
client.connect(('insert public IP address here', 600))
print('Connected!')

while True:
    # confirm message to stay synchronized with server
    client.send('confirmed'.encode())
    data = client.recv(1024)
    data = loads(data)
    
    # depending on the data type, control the mouse and keyboard accordingly
    if isinstance(data, list):
        x, y = data
        mouse.position = (x, y)

    # pynput has listeners for both mouseup and mousedown, so downButtons keeps
    # track of which buttons are still being pressed
    elif isinstance(data, Button):
        if data not in downButtons:
            downButtons.append(data)
            mouse.press(data)
        else:
            downButtons.remove(data)
            mouse.release(data)
            
    elif isinstance(data, int):
        mouse.scroll(0, data)
    
    # pynput has listeners for keyup and mousedown as well, so downKeys keeps
    # track of which keys are still being pressed
    elif isinstance(data, Key) or isinstance(data, KeyCode):
        if data not in downKeys:
            downKeys.append(data)
            keyboard.press(data)
        else:
            downKeys.remove(data)
            keyboard.release(data)

client.close()
