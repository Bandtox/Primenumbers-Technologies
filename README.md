# Web Scraping with Selenium and Python

##Introduction

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
 
### Edge WebDriver Setup

5. **If you haven't already, ensure that the Microsoft Edge WebDriver (`msedgedriver.exe`) is correctly placed in your project directory (`D:\Scrape\msedgedriver.exe` as specified in the script).**

**If the WebDriver isn't compatible with your Edge browser version, you can download the appropriate version from [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and replace it in your project directory.**

6. **Set WebDriver Path**: Update `webdriver_path` in the script with the path to `msedgedriver.exe`.

7. **Run the Script**: Execute the script using Python:
    ```python Scrape.py```


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
