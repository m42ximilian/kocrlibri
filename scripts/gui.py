import PySimpleGUI as sg
import threading
import keyboard
import asyncio
from navigation import navigate_ocr
from ocr import perform_ocr
from set_settings import *

"""
A module for integrating OCR-based navigation with a chatbox interface and system tray icon.

This module leverages PySimpleGUI for GUI components, threading for concurrent operations, and keyboard
for global keyboard shortcuts. It provides functionalities to open a chatbox window where users can enter
commands, use OCR (Optical Character Recognition) to find and navigate to text within images on the screen,
and modify application settings through a system tray icon.

Key functionalities include:
- `chatbox_window()`: An asynchronous function to display a chatbox window for command input.
- `open_chatbox()`: Opens the chatbox window and handles its operations in a non-blocking manner using asyncio and threading.
- `system_tray_icon()`: Creates a system tray icon with options to open the chatbox, adjust settings, or exit the application.
- `start_keyboard_listener()`: Starts a global keyboard listener for specific shortcuts to open the chatbox.

The module requires external navigation (`navigate_ocr`), OCR (`perform_ocr`), and settings management (`set_settings.py`) components.
"""

async def chatbox_window():
    layout = [[sg.Text("Enter command")], [sg.InputText()], [sg.Button("Run"), sg.Button("Cancel")]]
    window = sg.Window("Command Input", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            window.close()
            break
        if event == "Run" and values[0].lower() == "run":
            user_input = values[0]
            window.close()
            ocr_text = await perform_ocr()
            navigate_ocr(user_input, ocr_text)
            break

def open_chatbox():
    asyncio.run(chatbox_window())
    threading.Thread(target=chatbox_window, daemon=True).start()

def system_tray_icon():
	menu_def = ['BLANK', ['Open Chatbox', 'Settings', 'Exit']]
	tray = sg.SystemTray(menu=menu_def, filename=r'/Users/maximilianhild/code/kocrlibri/icon/kolibri.png')

	while True:
		event = tray.read()
		if event == 'Exit':
			break
		elif event == 'Open Chatbox':
			threading.Thread(target=open_chatbox, daemon=True).start()
					
		elif event == 'Settings':
			current_settings = read_settings()
			# Implement open_settings_window() to show a GUI dialog for settings modification
			new_settings = open_settings_window(current_settings)
			if new_settings:
				update_settings(new_settings)

	tray.close()

def on_press(key):
    try:
        # For macOS, listening for cmd+k
        if key == keyboard.Key.cmd and keyboard.KeyCode.from_char('k'):
            open_chatbox()
        # For Windows/Linux, listening for ctrl+k
        elif key == keyboard.Key.ctrl and keyboard.KeyCode.from_char('k'):
            open_chatbox()
    except AttributeError:
        pass

def start_keyboard_listener():
    # Start listening for the keyboard event
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

