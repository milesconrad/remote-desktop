from pickle import loads
from time import sleep
import p2py

from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
from pynput.keyboard._win32 import KeyCode

downKeys = []
downButtons = []
node = p2py.P2P_Node(601)

def handler(node, conn, request):
    data = request.contents['data']
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

node.add_handler('event', handler)
node.start()
node.join_network((('67.149.113.14', 600)))
while not node.connections:
	sleep(0.01) 