import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to the Edge WebDriver
webdriver_path = "msedgedriver.exe"

# Setup the Edge WebDriver using the Service class and headless options
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

service = Service(webdriver_path)
driver = webdriver.Edge(service=service, options=options)

retry_attempts = 3  # Number of retry attempts
retry_wait_time = 10  # Wait time in seconds between retries

try:
    attempt = 1
    while attempt <= retry_attempts:
        print(f"Attempting to open the website...")
        driver.get("https://hprera.nic.in/PublicDashboard")

        try:
            # Wait for the page to load completely by checking for a specific element
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[onclick^='tab_project_main_ApplicationPreview']"))
            )
            print("Page loaded successfully.")
            break  # Exit the retry loop if page loads successfully
        except Exception as e:
            print(f"Attempt {attempt}: Page load took too long. Retrying...")
            print(e)
            attempt += 1
            time.sleep(retry_wait_time)
    
    if attempt > retry_attempts:
        print("Exceeded retry attempts. Please re-run the program.")
    else:
        # Find all project cards
        print("Finding project cards...")
        cards = driver.find_elements(By.CSS_SELECTOR, "a[onclick^='tab_project_main_ApplicationPreview']")
        
        # Limit to the first 6 cards only
        print(f"Found {len(cards)} projects. Limiting to the first 6 registered projects.")
        
        # Extract details from each card
        data = []
        
        for index, card in enumerate(cards[:6]):
            print(f"Clicking on project {index + 1}...")
            # Click the card to load its details
            card.click()
            
            # Wait for the details to load
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//td[text()='Name']/following-sibling::td"))
                )
                
                # Extract the required details
                name = driver.find_element(By.XPATH, "//td[text()='Name']/following-sibling::td").text
                pan_no = driver.find_element(By.XPATH, "//td[text()='PAN No.']/following-sibling::td/span").text
                gstin_no = driver.find_element(By.XPATH, "//td[text()='GSTIN No.']/following-sibling::td/span").text
                address = driver.find_element(By.XPATH, "//td[text()='Permanent Address']/following-sibling::td/span").text
                
                # Store the details in a dictionary
                project_data = {
                    "Name": name,
                    "PAN No.": pan_no,
                    "GSTIN No.": gstin_no,
                    "Permanent Address": address
                }
                
                # Add the project data to the list
                data.append(project_data)
            except Exception as e:
                print(f"Failed to extract data from project {index + 1}: {e}")
            
            # Close the details view
            try:
                close_button = driver.find_element(By.XPATH, "//button[text()='Close']")
                if close_button:
                    close_button.click()
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "a[onclick^='tab_project_main_ApplicationPreview']"))
                    )
                else:
                    driver.back()
                    WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "a[onclick^='tab_project_main_ApplicationPreview']"))
                    )
                print(f"Closed details view for project {index + 1}")
            except Exception as e:
                print(f"Failed to close details view for project {index + 1}: {e}")
        
        # Specify the file path
        csv_file = 'output.csv'
    
        # Open the file in write mode ('w', newline='') to avoid extra blank lines
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
        print(f'CSV file "{csv_file}" has been created successfully.')

        print()
        print("Extracted data from all first 6 projects:")
        for project in data:
            print(project)
    
finally:
    # Close the browser
    print("Closing the browser...")
    driver.quit()
