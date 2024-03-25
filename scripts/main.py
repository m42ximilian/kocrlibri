from ocr import perform_ocr
from navigation import navigate_ocr
import asyncio
from create_logger import logger
from text_processing_ocr_output import * 
import sys

'''
Main function to trigger the OCR and navigation functions. Currently 
executed through the 'Fly' command in the status bar menu of kocrlibri.
'''
async def main():


	# Get the logger
	python_logger = logger('python_logger', '/Users/maximilianhild/code/kocrlibri/logs/logfile_python.txt')
	python_logger.info("Starting the main function.")

	await asyncio.sleep(1)

	iterations_data = [] 

	ocr_data_found = True
	scroll_count = 0  
	next_button_clicked = False
	max_iterations = 5

	while not next_button_clicked and scroll_count < max_iterations:
		await asyncio.sleep(5)
		ocrd_data = await perform_ocr()
		if len(ocrd_data) == 0:
			# End the loop and stop main function
			ocr_data_found = False
			python_logger.info("No OCR data found. Exiting main function.")
			break
		
		# await update_continuous_text_file(new_ocrd_data)
		next_button_clicked = await navigate_ocr(target_word="Next", ocr_data=ocrd_data)

		# After each OCR operation and before potentially breaking the loop, save the iteration data
		iterations_data.append({
			'scroll_count': scroll_count,
			'scroll_increment': 10,
			'ocr_data': ocrd_data
		})

		if not next_button_clicked:
			scroll_count += 1 

	if not ocr_data_found or scroll_count >= max_iterations:
		if scroll_count >= max_iterations:
			python_logger.info(f"Reached maximum iterations ({max_iterations}) without finding the target word.")  
		# Log or process the iterations_data as needed
		python_logger.info(f"Completed scanning with {len(iterations_data)} iterations.")

	# Add a clean exit point
	python_logger.info("Script has completed. Exiting now.")
	sys.exit(0)  # Cleanly exits the script

if __name__ == "__main__":
	asyncio.run(main())
