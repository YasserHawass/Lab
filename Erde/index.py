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
sleep(2)
# print (erdeSerial.readline(erdeSerial.inWaiting()))

top = tkinter.Tk()

def TrunOn():
  erdeSerial.write(b'50\r\n')
  # sleep(0.1)
  # data = erdeSerial.readline(erdeSerial.inWaiting())
  # label1.config(text=str(data))

def Turnoff():
  # erdeSerial.write((255, 'utf-8'))
  erdeSerial.write(b'1000\r\n')
  # print(bytes(1000))
  # sleep(0.1)
  # data = erdeSerial.readline(erdeSerial.inWaiting())
  # label1.config(text=str(data))

OnButton = tkinter.Button(top, text ="LED ON", command = TrunOn)
OffButton = tkinter.Button(top, text ="LED OFF", command = Turnoff)
label1 = Label(top, fg="green")

label1.pack()
OnButton.pack()
OffButton.pack()
top.mainloop()
