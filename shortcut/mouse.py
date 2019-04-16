from pynput import keyboard as pynputkeyboard
import keyboard         #external file
from pynput import mouse



def on_functionf8(key):
    if (key==pynputkeyboard.Key.f1):
        print('f8 is pressed')


key_listener = pynputkeyboard.Listener(on_release=on_functionf8)
key_listener.start()


def on_click(x, y, button, pressed):
    print("we in")
    if button == mouse.Button.left:
        print ('Left')

    if button == mouse.Button.right:
        key_listener.stop()
        print ('right')
    if button == mouse.Button.middle:
        print ('middle')

with mouse.Listener(on_click=on_click) as MouseListener:
        MouseListener.join()
