import json
import PySimpleGUI as sg

def read_settings():
	try:
		with open('settings.json', 'r') as file:
			settings = json.load(file)
			return settings
	except FileNotFoundError:
		print("Settings file not found. Using default settings.")
		return {"screenshot_path": "/default/path/to/screenshots"}


def update_settings(new_settings):
	try:
		with open('settings.json', 'w') as file:
			json.dump(new_settings, file, indent=4)
	except Exception as e:
		print(f"Failed to update settings: {e}")


def open_settings_window(current_settings):
	layout = [
		[sg.Text('Screenshot Path:'), sg.InputText(current_settings['screenshot_path'], key='SCREENSHOT_PATH')],
		[sg.Button('Save'), sg.Button('Cancel')]
	]

	window = sg.Window('Settings', layout)

	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED or event == 'Cancel':
			break
		if event == 'Save':
			new_settings = {'screenshot_path': values['SCREENSHOT_PATH']}
			update_settings(new_settings)
			break

	window.close()

	if event == 'Save':
		return new_settings
	else:
		return None

