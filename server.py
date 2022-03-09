from time import time
from pickle import dumps
import socket
from pynput import mouse
from pynput import keyboard

server = socket.socket()
server.bind(('insert local IP address here', 600))
server.listen(2)
print('Listening...')
connection, address = server.accept()
print('New connection from ' + address[0])

last_moved = time()

def on_move(x, y):
    last_moved
    if time() - last_moved > 0.1:
        connection.recv(1024)
        mouse_position = dumps([x, y])
        connection.send(mouse_position)
        last_moved = time()

def on_click(x, y, pressed_button, pressed):
    connection.recv(1024)
    pressed_button = dumps(pressed_button)
    connection.send(pressed_button)

def on_scroll(x, y, x_direction, y_direction):
    connection.recv(1024)
    y_direction = dumps(y_direction)
    connection.send(y_direction)

def on_press(pressed_key):
    connection.recv(1024)
    pressed_key = dumps(pressed_key)
    connection.send(pressed_key)

def on_release(released_key):
    connection.recv(1024)
    released_key = dumps(released_key)
    connection.send(released_key)

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
connection.close()
