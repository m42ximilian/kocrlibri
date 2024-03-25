# kocrlibri
## Researching OCR and LLM functionality for web browser automation

### Setup
* Create virtual environemnt (not necessary, but recommended)
	- python version=3.10
	- for packages see requirements.txt
	- [install tesseract](https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file#installing-tesseract)
* Clone repository
* Run python start_gui_in_mac_os.py

### Implemented core functionality:
* Navigation through MacOS native GUI
* Toggle screenshot taking from menu bar app
* Perform OCR on screenshot and extract data for navigation
* Navigate to next page from menu bar app using *Fly* command
	- currently works by scrolling through entire page (max_iterations parameter in main.py) and manually declaring the next button (navigate_ocr() paramter in main.py)

### Benchmarks:
* Scraping LinkedIn
* Scraping Blinkist
* Scraping Amazon

### TODO: 
* Terminating *Fly* command from menu bar
* Integrate LLM to make sense of OCR output
* Fine-tune browsing automation:
	- find website navigation autonomously 
	- detect top and bottom edges of page
	- ignore rest of browser 

* Integrate realisitic mouse movements and keyboard stroke - as in simulating user browsing behavior

### Ideas:
* Implementing some sort of compression and storage system for input files --> desiding to use images or OCR output
* Integrate Playwright for background browser automations on pages which allow for it
* Integrate webUI classification to optimise for scraping and browsing targets?
* Integrate web search through langchain
* Integrate pdf recognition
* Integrate audio transcription for video-calls

* This could be turned into a system-wide personal assistant that:
	- does research tasks for you in the background 
	- writes summaries of you work, meetings, calls (like unlost.ai, rewind.ai)
	- can help with smart-scheduling work with 
		- keeping track of your productivity windows
		- knowing your calendar