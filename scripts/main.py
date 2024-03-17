from ocr import perform_ocr
from navigation import navigate_ocr
import asyncio
from create_logger import logger


async def main():

	# Get the logger
	python_logger = logger('python_logger', '/Users/maximilianhild/code/kocrlibri/logs/logfile_python.txt')
	python_logger.info("Starting the main function.")

	await asyncio.sleep(1)

	ocr_data = await perform_ocr()
	navigate_ocr(target_word='Next', ocr_data=ocr_data)


if __name__ == "__main__":
	asyncio.run(main())

