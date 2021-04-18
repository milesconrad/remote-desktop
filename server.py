from pickle import dumps
import socket
from pynput import mouse
from pynput import keyboard

server = socket.socket()
server.bind(('insert local IP address here', 600))
server.listen(2)
print('Listening...')
conn, address = server.accept()
print('New connection from ' + address[0])

def on_move(x, y):
    conn.recv(1024)
    position = dumps([x, y])
    conn.send(position)

def on_click(x, y, button, pressed):
    conn.recv(1024)
    button = dumps(button)
    conn.send(button)

def on_scroll(x, y, dx, dy):
    conn.recv(1024)
    direction = dumps(dy)
    conn.send(direction)

def on_press(key):
    conn.recv(1024)
    key = dumps(key)
    conn.send(key)

def on_release(key):
    conn.recv(1024)
    key = dumps(key)
    conn.send(key)

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
conn.close()
