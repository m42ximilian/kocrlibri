import asyncio
import json
import logging
import pyautogui

logger = logging.getLogger('python_logger')

async def navigate_ocr(target_word, ocr_data=None):
	if ocr_data is None:
		logger.error("No OCR data provided.")
		return False

	loop = asyncio.get_running_loop()
	found = False

	for item in ocr_data:
		if item['text'] == target_word:
			x, y, w, h = item['left'], item['top'], item['width'], item['height']
			x /= 2  # Adjust for Retina display
			y /= 2
			center_x, center_y = x + w / 2, y + h / 2

			# Non-blocking moveTo and click
			await loop.run_in_executor(None, pyautogui.moveTo, center_x, center_y, 2)
			await loop.run_in_executor(None, pyautogui.click, center_x, center_y)
			
			found = True
			logger.info(f"Clicked on '{target_word}' at ({center_x}, {center_y}).")
			break  # Remove this break to click on all occurrences of the word

	if not found:
		logger.info(f"The word '{target_word}' was not found in the provided OCR data.")
		await loop.run_in_executor(None, pyautogui.scroll, -10)  # Non-blocking scroll
	
	return found

async def main():
	ocr_data_path = "/Users/maximilianhild/code/kocrlibri/ocr_out/ocr_screenshot_2024-03-27_10-47-02.json"
	with open(ocr_data_path, 'r') as file:
		ocr_data = json.load(file)
	await navigate_ocr(target_word="Next", ocr_data=ocr_data)

if __name__ == '__main__':
	asyncio.run(main())
