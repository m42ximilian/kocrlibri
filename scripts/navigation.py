import pytesseract
import pyautogui

def navigate_ocr(target_word, ocr_text=None):
	"""
    Navigates to and clicks on the specified target word within an image using OCR data.

    This function checks if the target word is present in the provided OCR text. If found, it uses pytesseract
    to extract the position data of the word in the image, calculates the center of the word's bounding box,
    and then moves the mouse to this position and clicks.

    Parameters:
        target_word (str): The word to navigate to and click on.
        ocr_text (str, optional): The OCR text obtained from an image. If not provided, a warning is printed.

    Note:
        - The function assumes a Retina display and adjusts the coordinates accordingly.
        - It only clicks the first occurrence of the word. Remove the break statement to click on all occurrences.
    """
    
	if ocr_text is None:
        
		print("No recognized text provided.")
	else:
		# Check if the word exists in the recognized text
		if target_word in ocr_text:
			# Find the position of the word in the image
			data = pytesseract.image_to_data(ocr_text, output_type=pytesseract.Output.DICT)
			word_occurrences = [i for i, word in enumerate(data['text']) if word == target_word]
			
			for occ in word_occurrences:
				# Extract the bounding box of the word
				x, y, w, h = data['left'][occ], data['top'][occ], data['width'][occ], data['height'][occ]
				
				# Changing ratio to fit retina display
				x /= 2
				y /= 2
				
				# Calculate the center of the bounding box
				center_x, center_y = x + w / 2, y + h / 2
				
				# Move the mouse to the center of the word and click
				pyautogui.moveTo(center_x, center_y, duration=2)
				pyautogui.click(center_x, center_y)
				break  # Remove this break if you want to click on all occurrences of the word
		else:
			print(f"The word '{target_word}' was not found in the screenshot.")
