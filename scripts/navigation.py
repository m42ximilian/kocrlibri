import logging
import pyautogui

def navigate_ocr(target_word, ocr_data=None):
    """
    Navigates to and clicks on the specified target word using pre-processed OCR data.
    
    This function assumes that `ocr_data` is a list of dictionaries, where each dictionary contains
    'text', 'left', 'top', 'width', and 'height' keys for each recognized word.

    Parameters:
        target_word (str): The word to navigate to and click on.
        ocr_data (list of dict, optional): Pre-processed OCR data including positional information. Each dict should have
                                            'text', 'left', 'top', 'width', 'height' keys.

    Note:
        - The function assumes a Retina display and adjusts the coordinates accordingly.
        - It only clicks the first occurrence of the word. To click on all occurrences, remove the break statement.
    """

    logger = logging.getLogger('python_logger')

    if ocr_data is None:
        logger.error("No OCR data provided.")
        return

    found = False
    for item in ocr_data:
        if item['text'] == target_word:
            x, y, w, h = item['left'], item['top'], item['width'], item['height']
            
            # Adjust for Retina display
            x /= 2
            y /= 2
            
            # Calculate the center of the bounding box
            center_x, center_y = x + w / 2, y + h / 2
            
            # Move the mouse to the center of the word and click
            pyautogui.moveTo(center_x, center_y, duration=2)
            pyautogui.click(center_x, center_y)
            found = True
            logger.info(f"Clicked on '{target_word}' at ({center_x}, {center_y}).")
            break  # Remove this break to click on all occurrences of the word

    if not found:
        logger.info(f"The word '{target_word}' was not found in the provided OCR data.")
