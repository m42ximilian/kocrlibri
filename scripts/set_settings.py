import json
'''
To be implemented: 
	- Integration of settings.json with macOS GUI
	- Not clear as of yet which settings will be relevant to set other than the screenshot path
'''

def read_settings():
    with open('/Users/maximilianhild/code/kocrlibri/scripts/settings.json', 'r') as file:
        settings = json.load(file)
    return settings