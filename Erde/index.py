# https://pythonhosted.org/pyserial/examples.html
# https://pythonhosted.org/pyserial/pyserial_api.html
# https://www.programiz.com/python-programming/methods/built-in/bytes
# https://docs.python.org/3/library/stdtypes.html

import tkinter
from tkinter import *
import serial
from time import sleep

# Enter your COM port in the below line
erdeSerial = serial.Serial('com3', 9600)

top = tkinter.Tk()

def DebugA():
    print(str(erdeSerial.readline().decode().strip('\r\n')).split('/'))

def Notificaion():
    erdeSerial.write(b'50')
def Reset():
    erdeSerial.write(b'1000')

NotificaionButton = tkinter.Button(top, text ="Notificaion!", command = Notificaion)
ResetButton = tkinter.Button(top, text ="Reset", command = Reset)
DebugAButton = tkinter.Button(top, text ="debug", command = DebugA)

NotificaionButton.pack()
ResetButton.pack()
DebugAButton.pack()
top.mainloop()


# # https://pythonhosted.org/pyserial/examples.html
# # https://pythonhosted.org/pyserial/pyserial_api.html
# # https://www.programiz.com/python-programming/methods/built-in/bytes
# # https://docs.python.org/3/library/stdtypes.html
#
# import tkinter
# from tkinter import *
# import serial
# from time import sleep
#
# # Enter your COM port in the below line
# erdeSerial = serial.Serial('com3', 9600)
# # sleep(2)
# # print (erdeSerial.readline(erdeSerial.inWaiting()))
#
# top = tkinter.Tk()
#
# def DebugA():
#     print(erdeSerial.readline().decode())
#
# def Notificaion():
#     erdeSerial.write(b'50')
#   # sleep(0.1)
#   # data = erdeSerial.readline(erdeSerial.inWaiting())
#   # label1.config(text=str(data))
#
# def Reset():
#   # erdeSerial.write((255, 'utf-8'))
#   erdeSerial.write(b'1000')
#   # print(bytes(1000))
#   # sleep(0.1)
#   # data = erdeSerial.readline(erdeSerial.inWaiting())
#   # label1.config(text=str(data))
#
# OnButton = tkinter.Button(top, text ="LED ON", command = Notificaion)
# OffButton = tkinter.Button(top, text ="LED OFF", command = Reset)
# DebugAButton = tkinter.Button(top, text ="debug", command = DebugA)
# # label1 = Label(top, fg="green")
#
# # label1.pack()
# Notificaion.pack()
# Reset.pack()
# DebugAButton.pack()
# top.mainloop()
