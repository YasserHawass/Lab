#https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/
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
from pynput import keyboard
from subprocess import call

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='a')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A')}
]

def VolumeUp():
    try:
            call(["amixer", "-D", "pulse", "sset", "Master", "5%+"])
    except ValueError:
        pass

# The currently active modifiers
current = set()

def execute():
    print ("Do Something")
    VolumeUp()

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
