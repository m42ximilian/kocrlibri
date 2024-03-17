import cv2
import os
import asyncio
import logging
import pytesseract
from pathlib import Path
from set_settings import read_settings

async def perform_ocr():
	"""
	Performs Optical Character Recognition (OCR) on the newest screenshot found in the `screenshot_buffer` folder,
	and returns structured OCR data.

	This asynchronous function reads settings to obtain the screenshot folder path, finds the newest screenshot in the folder, 
	and then uses pytesseract to perform OCR on this image. It returns structured OCR data that includes positional 
	information for each recognized word.

	Returns:
		A list of dictionaries, where each dictionary contains 'text', 'left', 'top', 'width', and 'height' keys for 
		each recognized word.

	Note:
		- The function reads 'screenshot_path' from a settings object obtained via read_settings(), which should point 
		to the folder containing the screenshots.
		- If no images are found in the folder, it logs an error message and returns an empty list.
	"""

	logger = logging.getLogger('python_logger')
	settings = read_settings()
	screenshot_folder_path = settings.get("screenshot_path")

	if not Path(screenshot_folder_path).is_dir():
		logger.error(f"Screenshot folder path does not exist: {screenshot_folder_path}")
		return []

	newest_screenshot = max(Path(screenshot_folder_path).glob('*.png'), key=os.path.getctime, default=None)

	if newest_screenshot is None:
		logger.error("No screenshot found in the folder.")
		return []

	screenshot_path = str(newest_screenshot)
	logger.info(f"Using newest screenshot at: {screenshot_path}")

	# Asynchronously perform OCR on the screenshot to obtain structured data
	async def do_ocr():
		image = cv2.imread(screenshot_path)
		if image is None:
			logger.error("Failed to load image for OCR.")
			return []

		# Convert image to grayscale for better OCR accuracy
		gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		ocr_result = pytesseract.image_to_data(gray_image, output_type=pytesseract.Output.DICT)

		# Structure OCR data for each recognized word
		ocr_data = [{'text': ocr_result['text'][i],
					'left': ocr_result['left'][i],
					'top': ocr_result['top'][i],
					'width': ocr_result['width'][i],
					'height': ocr_result['height'][i]}
					for i in range(len(ocr_result['text']))
					if ocr_result['text'][i].strip() != '']  # Exclude empty strings

		return ocr_data

	loop = asyncio.get_running_loop()
	structured_ocr_data = await do_ocr()

	return structured_ocr_data
