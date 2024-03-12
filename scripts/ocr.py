import asyncio
import pyautogui
import pytesseract
import cv2
from concurrent.futures import ThreadPoolExecutor

from settings import read_settings

async def perform_ocr():
	"""
    Performs Optical Character Recognition (OCR) on a screenshot of the entire screen.

    This asynchronous function reads settings to obtain a screenshot path, takes a screenshot of the entire screen, 
    saves it, and then uses pytesseract to perform OCR on the saved image. It handles the screenshot capture 
    and OCR processing in a non-blocking way using asyncio and ThreadPoolExecutor, ensuring the event loop 
    is not blocked during these operations.

    Returns:
        A future object representing the OCR'd text from the screenshot. The actual text can be obtained by 
        awaiting this future.

    Note:
        - The function reads 'screenshot_path' from a settings object obtained via read_settings().
        - It waits for 2 seconds after taking the screenshot to ensure the file is saved before attempting OCR.
        - If the screenshot cannot be loaded, it prints an error message and returns an empty string.
    """

	# Read the current settings to get the screenshot path
	settings = read_settings()
	screenshot_path = settings.get("screenshot_path")

	loop = asyncio.get_running_loop()

	# Take a screenshot of the entire screen in a non-blocking way
	await loop.run_in_executor(None, pyautogui.screenshot, screenshot_path)

	# Wait for a brief period to ensure the screenshot has been saved
	await asyncio.sleep(2)

	# Define a helper function to the asynchroneous OCR
	def do_ocr():
		# Use pytesseract to do OCR on the screnshot
		image = cv2.imread(screenshot_path)
		if image is None:
			print("Failed to load image. Check file path and integrity.")
			return ''
		else:
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			text = pytesseract.image_to_string(gray)
			return text

	# Run the CPU-bound tasks in a thread executor to avoid blocking the event loop
	text = loop.run_in_executor(None, do_ocr)

	return text
