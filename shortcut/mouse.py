from pynput import mouse

def on_click(x, y, button, pressed):
    if button == mouse.Button.middle:
        print ('middle')

with mouse.Listener(on_click=on_click) as MouseListener:
        MouseListener.join()
