# Web Scraping with Selenium and Python

This script uses Selenium WebDriver to scrape data from a website and extract project details into a CSV file.

## Requirements

- Python 3.x
- Selenium WebDriver
- Microsoft Edge WebDriver (`msedgedriver.exe`)

## Installation

1. **Install Python**: If you haven't already, install Python from [python.org](https://www.python.org/downloads/).

2. **Install Selenium**: Install Selenium using pip:
  `pip install selenium`
 
3. **Download Edge WebDriver**: Download the Microsoft Edge WebDriver compatible with your Edge browser version from [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

4. **Set WebDriver Path**: Update `webdriver_path` in the script with the path to `msedgedriver.exe`.

5. **Run the Script**: Execute the script using Python:
    `python Scrape.py`


## Script Details

- **WebDriver Setup**: Sets up the Edge WebDriver in headless mode with specified options.
- **Page Load Retry**: Attempts to load the target webpage with retry mechanism and waits for specific elements to appear.
- **Data Extraction**: Extracts project details such as Name, PAN No., GSTIN No., and Permanent Address from project cards.
- **CSV Output**: Writes the extracted data into a CSV file named `output.csv`.
- **Error Handling**: Includes basic error handling and retry logic for robustness.

## Notes

- Adjust `retry_attempts` and `retry_wait_time` variables for your network conditions.
- Ensure compatibility of Edge WebDriver with your Edge browser version.

Feel free to modify the script as needed for your specific scraping requirements.
