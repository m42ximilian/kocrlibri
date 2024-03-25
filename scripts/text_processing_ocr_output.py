import aiofiles
import asyncio
import json
from set_settings import read_settings

'''
Extract Text: Extract the text from both OCR outputs. Assuming each OCR output is a list of 
dictionaries containing 'text' and positional keys ('left', 'top', 'width', 'height'), you 
would focus on the 'text' field.

Compare and Remove Duplicates: Compare the text entries from the second OCR output against 
those in the first. Any duplicates found in the second output, based solely on the 'text' 
content, would be removed. This comparison could be case-sensitive or case-insensitive, 
depending on your requirements.

Keep Positional Integrity: If your final goal requires maintaining positional integrity 
(e.g., for document layout purposes), you might also consider the positional information
during the comparison. However, for a simple text concatenation based on content, comparing 
the 'text' fields alone suffices.

Here's a basic implementation that compares the text fields and removes duplicates from 
the second OCR output, ignoring case sensitivity:
'''

# Function to read settings from the settings.json file
# def read_settings():
#     with open('settings.json', 'r') as file:
#         settings = json.load(file)
#     return settings

def remove_duplicate_text_from_ocr_output(ocr_output1, ocr_output2):
	
	if ocr_output1:
		# Extract text content from the first OCR output
		texts1 = set([entry['text'].lower() for entry in ocr_output1])
		
		# Filter out duplicates from the second OCR output
		unique_ocr_output2 = [entry for entry in ocr_output2 if entry['text'].lower() not in texts1]
		
		return unique_ocr_output2

# Example usage
# ocr_output1 = [{'text': 'Hello', 'left': 10, 'top': 10, 'width': 50, 'height': 20},
# 			{'text': 'world', 'left': 70, 'top': 10, 'width': 50, 'height': 20}]
# ocr_output2 = [{'text': 'world', 'left': 10, 'top': 40, 'width': 50, 'height': 20},
# 			{'text': 'Goodbye', 'left': 70, 'top': 40, 'width': 60, 'height': 20}]

# Remove duplicates from ocr_output2 that are present in ocr_output1
# unique_ocr_output2 = remove_duplicate_text_from_ocr_output(ocr_output1, ocr_output2)
# print(unique_ocr_output2)


async def read_continuous_text_file(filepath):
	async with aiofiles.open(filepath, mode='r') as file:
		return await file.read()

async def update_continuous_text_file(new_texts):
    settings = read_settings()
    filepath = settings["continuous_text_filepath"]
    
    async with aiofiles.open(filepath, 'r') as file:
        existing_text = await file.read()
    existing_lines = set(existing_text.splitlines())
    
    unique_new_texts = [text for text in new_texts if text not in existing_lines]
    
    if unique_new_texts:
        updated_text = existing_text + '\n' + ('\n'.join(unique_new_texts) if existing_text else '\n'.join(unique_new_texts).lstrip())
        async with aiofiles.open(filepath, 'w') as file:
            await file.write(updated_text)
