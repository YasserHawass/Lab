#https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/
from pynput import keyboard as pynputkeyboard
import keyboard         #external file


# The key combination to check
COMBINATIONS = [
    {pynputkeyboard.Key.shift, pynputkeyboard.KeyCode(char='a')},
    {pynputkeyboard.Key.shift, pynputkeyboard.KeyCode(char='A')}
]

COMBINATIONZ = [
    {pynputkeyboard.Key.shift, pynputkeyboard.KeyCode(char='z')},
    {pynputkeyboard.Key.shift, pynputkeyboard.KeyCode(char='Z')}
]

MUTE = [
    {pynputkeyboard.Key.shift, pynputkeyboard.KeyCode(char='q')},
    {pynputkeyboard.Key.shift, pynputkeyboard.KeyCode(char='Q')}
]


# The currently active modifiers
current = set()
def on_press(key
    #update here 1
    if any([key in COMBO for COMBO in COMBINATIONS]) or any([key in COMBO for COMBO in COMBINATIONZ]) or any([key in COMBO for COMBO in MUTE]):
        current.add(key)
        #update here 2, add the func in keyboard 4
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            keyboard.VolumeUp()
        elif any(all(k in current for k in COMBO) for COMBO in COMBINATIONZ):
            keyboard.VolumeDown()
        elif any(all(k in current for k in COMBO) for COMBO in MUTE):
            keyboard.Mute()

def on_release(key):
    #update here 3
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONZ]):
        current.remove(key)
    elif any([key in COMBO for COMBO in MUTE]):
        current.remove(key)

with pynputkeyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()













###############################################################
# from pynput import keyboard
#
# # The currently active modifiers
# current = set()
#
#
# def on_press(key):
#     pass
#
# def on_release(key):
#     pass
#
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
#
# # The key combination to check
# COMBINATIONS = [
#     {keyboard.Key.shift, keyboard.KeyCode(char='a')},
#     {keyboard.Key.shift, keyboard.KeyCode(char='A')}
# ]
#
# def execute():
#     print ("Do Something")
#
# def on_press(key):
#     if any([key in COMBO for COMBO in COMBINATIONS]):
#         current.add(key)
#         if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
#             execute()
# def on_release(key):
#     if any([key in COMBO for COMBO in COMBINATIONS]):
#         current.remove(key)
#################################################################################################################
