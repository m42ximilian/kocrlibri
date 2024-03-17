# kocrlibri
## Researching OCR and LLM functionality for web browser automation

### Implemented core functionality:
* Navigation through MacOS native GUI
* Take a screenshot from menu bar app
* Perform OCR on screenshot and extract data for navigation
* Navigate to next page from menu bar app using *Fly* command
* Leverage LLM to make sense of OCR output

### Benchmarks:
* Scraping LinkedIn
* Scraping Blinkist
* Scraping Amazon

### TODO: 
* Implement complete browsing automation:
	- taking many snapshots
	- while scrolling through page
	- concantenate and extract data
	- go to next page

* Integrate realisitic mouse movements and keyboard stroke - as in simulating user browsing behavior
* Integrate better chatbot to give instructions to script
* Integrate langchain 
  

### Ideas:
* Integrating Selenium for background browser automations on pages which allow for it
* Integrate webUI classification to optimise for scraping and browsing targets

* This could be turned into a system-wide personal assistant that:
	- does research tasks for you in the background 
	- writes summaries of you work, meetings, calls (like unlost.ai, rewind.ai)
	- can help with smart-scheduling work with 
		- keeping track of your productivity windows
		- knowing your calendar