from pickle import dumps
import p2py
from pynput import mouse, keyboard

node = p2py.Node(600)
def new_connection(node, conn, request):
    print(conn)
node.add_handler('connected', new_connection)
msg = {'type' : 'event'}
node.start()
print('Listening...')

def on_move(x, y):
    position = dumps([x, y])
    msg['data'] = position
    node.send_to_UUID(UUID=1, msg=msg)

def on_click(x, y, button, pressed):
    button = dumps(button)
    msg['data'] = button
    node.send_to_UUID(UUID=1, msg=msg)

def on_scroll(x, y, dx, dy):
    direction = dumps(dy)
    msg['data'] = direction
    node.send_to_UUID(UUID=1, msg=msg)

def on_press(key):
    key = dumps(key)
    msg['data'] = key
    node.send_to_UUID(UUID=1, msg=msg)

def on_release(key):
    key = dumps(key)
    msg['data'] = key
    node.send_to_UUID(UUID=1, msg=msg)

mouseListener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
keyboardListener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
mouseListener.start()
keyboardListener.start()

mouseListener.join()
keyboardListener.join()