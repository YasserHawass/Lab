from pynput import mouse as pynputmouse

test = {pynputmouse.Button.middle, pynputmouse.Button.right}
currentm = set()

def on_click(x, y, button, pressed):
    if pressed and button in test:
        currentm.add(button)
        if all(k in currentm for k in test):
            print ('middleX')
            currentm.clear()

with pynputmouse.Listener(on_click=on_click) as MouseListener:
        MouseListener.join()





# from pynput import mouse as pynputmouse
#
# test = {pynputmouse.Button.middle, pynputmouse.Button.right}
# currentm = set()
#
# def on_click(x, y, button, pressed):
#     # print (button)
#     # print (currentm)
#     if pressed and button in test:
#         currentm.add(button)
#         # if button == pynputmouse.Button.middle:
#         #     print ('middle')
#         #     # MouseListener.stop()
#         if all(k in currentm for k in test):
#             print ('middleX')
#             currentm.clear()
#     # elif (pynputmouse.Button.middle and pynputmouse.Button.left):
#     #         print("Woah")
#     # elif not pressed:
#     #     # Stop listener
#     #     return False              stops the app
#
# with pynputmouse.Listener(on_click=on_click) as MouseListener:
#         MouseListener.join()
#
#

#
#
#
#
# from pynput import keyboard
#
# # The key combination to check
# COMBINATION = {keyboard.Key.cmd, keyboard.Key.ctrl}
#
# # The currently active modifiers
# current = set()
#
#
# def on_press(key):
#     if key in COMBINATION:
#         current.add(key)
#         if all(k in current for k in COMBINATION):
#             print('All modifiers active!')
#     if key == keyboard.Key.esc:
#         listener.stop()
#
#
# def on_release(key):
#     try:
#         current.remove(key)
#     except KeyError:
#         pass
#
#
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
