import objc
from Cocoa import NSApplication, NSApp, NSStatusBar, NSMenu, NSMenuItem, NSVariableStatusItemLength, NSImage
from PyObjCTools.AppHelper import NSApplicationMain, NSObject
import sys
import os 
import subprocess
from create_logger import logger

"""
A macOS status bar application created with PyObjC that provides quick access to a set of functionalities such as
executing a predefined script, taking screenshots, and opening a chat interface. 

The application embeds a status item in the macOS system status bar with a custom icon and a menu offering several 
actions: 
"Fly" to run a specific Pythonscript, 
"Take Screenshot" to capture the screen, 
"Open Chat" to presumably open a chat interface, 
along with "Settings" and "Quit" options. 
Logging is configured for monitoring the  application's operations. This example illustrates the use of NSStatusBar, 
NSMenuItem, and subprocesses within a  PyObjC-based application, showcasing how to integrate Python code with native 
macOS APIs for desktop automation tasks.
"""


# Configure logging
swift_logger = logger('swift_logger', '/Users/maximilianhild/code/kocrlibri/logs/logfile_swift.txt')


class AppDelegate(NSObject):
	def applicationDidFinishLaunching_(self, notification):
		self.statusItem = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength)
		if self.statusItem.button():
			# Create an NSImage object from the image file
			image = NSImage.alloc().initWithContentsOfFile_("/Users/maximilianhild/code/kocrlibri/icon/kolibri_white.png")
			self.statusItem.button().setImage_(image)
			#self.statusItem.button().setTitle_("👽")
		
		self.setupMenus()

	def setupMenus(self):
		menu = NSMenu.alloc().init()

		flyMenuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("Fly", "runScript:", "k")
		menu.addItem_(flyMenuItem)
		flyMenuItem.setTarget_(self)  # Set the target for the action

		# Add Take Screenshot menu item
		screenshotMenuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("Take Screenshot", "takeScreenshot:", "s")
		menu.addItem_(screenshotMenuItem)
		screenshotMenuItem.setTarget_(self)

		openMenuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("Open Chat", "openChat:", "o")
		menu.addItem_(openMenuItem)

		menu.addItem_(NSMenuItem.separatorItem())

		settingsMenuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("Settings", None, "s")
		menu.addItem_(settingsMenuItem)

		quitMenuItem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("Quit", "terminate:", "q")
		menu.addItem_(quitMenuItem)
		quitMenuItem.setTarget_(NSApp)

		self.statusItem.setMenu_(menu)

	@objc.IBAction
	def runScript_(self, sender):
		# Path to the current script (your PyObjC application)
		current_script_path = os.path.dirname(os.path.realpath(__file__))
		
		# Name of the script you want to run
		script_name = "main.py"
		
		# Construct the full path to the script
		script_path = os.path.join(current_script_path, script_name)
		
		# Use subprocess to run the script
		try:
			subprocess.run(["python", script_path], check=True)
			success_message = f"Script {script_name} executed successfully."

			# Log the success message along with the script path
			swift_logger.info(f"{success_message} Path: {script_path}")
			
		except subprocess.CalledProcessError as e:
			error_message = f"Error executing script {script_name}: {e}"
			
			# Log the error message along with the script path
			swift_logger.error(f"{error_message} Path: {script_path}")


	@objc.IBAction
	def takeScreenshot_(self, sender):

		# Define the directory where you want to save the screenshot
		screenshots_dir = "/Users/maximilianhild/code/kocrlibri/screenshot_buffer"
		if not os.path.exists(screenshots_dir):
			os.makedirs(screenshots_dir)

		# Create a unique file name for the screenshot
		from datetime import datetime
		timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
		screenshot_path = os.path.join(screenshots_dir, f"screenshot_{timestamp}.png")


		# Define the command and arguments for taking a screenshot
		command = "/usr/sbin/screencapture"
		args = ["-x", screenshot_path]  # '-w' waits for a window selection, saves to screenshot_path

		# Execute the command
		try:
			subprocess.run([command] + args, check=True)
			swift_logger.info(f"Screenshot taken successfully and saved to {screenshot_path}.")
		except subprocess.CalledProcessError as e:
			swift_logger.error(f"Error taking screenshot: {e}")


	@objc.python_method	
	def openChat_(self, sender):
		# Code to open chat box
		print("Open Chat menu item clicked.")



if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    NSApplicationMain(sys.argv)
