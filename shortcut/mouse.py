from pynput import mouse as pynputmouse

# test = [
#     {pynputmouse.Button.right, pynputmouse.Button.left}
# ]
# currentm = set()

def on_click(x, y, button, pressed):
    if pressed:
        if button == pynputmouse.Button.middle:
            print ('middle')
        # elif any(all(k in currentm for k in COMBO) for COMBO in test):
        #     print ('middleX')
    # elif (pynputmouse.Button.middle and pynputmouse.Button.left):
    #         print("Woah")
    # elif not pressed:
    #     # Stop listener
    #     return False              stops the app

with pynputmouse.Listener(on_click=on_click) as MouseListener:
        MouseListener.join()
