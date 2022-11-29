# importing required module
from playsound import playsound

# making function
def play():
	playsound('assets/alert.mp3')

# hello_psg.py

import PySimpleGUI as sg

layout = [[sg.Text("Under Attack")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Intrusion Detection System", layout)
play()
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or     # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()