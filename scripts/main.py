from gui import *

def main():
		
	# Start the keyboard listener in a separate thread
    listener_thread = threading.Thread(target=start_keyboard_listener, daemon=True)
    listener_thread.start()

    # Start the system tray icon (which can also open the chatbox)
    system_tray_icon()


if __name__ == "__main__":
	main()