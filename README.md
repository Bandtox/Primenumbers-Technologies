# Web Scraping with Selenium and Python

## Introduction

This Python script utilizes Selenium to scrape data from the HPRERA Public Dashboard. It retrieves details of the first 6 projects under the "Registered Projects" section, including GSTIN No., PAN No., Name, and Permanent Address.

## Requirements

- Python 3.x
- Selenium WebDriver
- Microsoft Edge WebDriver (`msedgedriver.exe`)

## Installation

1. **Install Python**: If you haven't already, install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**
   ```bash
   git clone https://github.com/Bandtox/Primenumbers-Technologies.git
   

4. **Install Selenium**: Install Selenium using pip:
   ```bash
   pip install selenium
 
5. **Edge WebDriver Setup**: Ensure the Microsoft Edge WebDriver executable (`msedgedriver.exe`) is correctly placed in the project directory (already included for convenience). If not compatible, download the compatible version for your Edge browser from [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and place it in the directory specified by `webdriver_path` in the Python script (for example `"D:\Primenumbers-Technologies\msedgedriver.exe"` or  `"\msedgedriver.exe"`, line 11).

6. **Run the Script**: Execute the script using Python:
    ```bash
    python Scrape.py

## Script Details

- **WebDriver Setup**: Sets up the Edge WebDriver in headless mode with specified options.
- **Page Load Retry**: Attempts to load the target webpage with retry mechanism and waits for specific elements to appear.
- **Data Extraction**: Extracts project details such as Name, PAN No., GSTIN No., and Permanent Address from project cards.
- **CSV Output**: Writes the extracted data into a CSV file named `output.csv`.
- **Error Handling**: Includes basic error handling and retry logic for robustness.

## Notes

- Adjust `retry_attempts` and `retry_wait_time` variables for your network conditions.
- Ensure compatibility of Edge WebDriver with your Edge browser version.

