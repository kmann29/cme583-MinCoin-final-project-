from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import os
import time

'''
Please note that the code was not able to change the page numbers, 
It was done manually by changing the number in the link/url seen on line 19 below
'''

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL to start scraping
url = "https://www.msha.gov/data-and-reports/fatality-reports/search?combine=&field_mine_category_target_id=191&year=all&location_node_administrative_area=All&page=1" #change page number
driver.get(url)

# Create directory for PDFs
os.makedirs('pdfs', exist_ok=True)

# Loop through all pages
while True:
    # Find all "Preliminary Report" links on the current page
    report_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Preliminary Report for")

    # Loop through each report link, refreshing `report_links` each time
    for i in range(len(report_links)):
        # Refresh the report links on the page each time, since the DOM may have changed
        report_links = driver.find_elements(By.PARTIAL_LINK_TEXT, "Preliminary Report for")

        # Click the report link to open the report page
        report_links[i].click()
        time.sleep(3)  # Wait for the page to load

        # Find and download the PDF
        try:
            pdf_url = driver.find_element(By.XPATH, "//a[contains(@href, '.pdf')]").get_attribute("href")
            pdf_name = pdf_url.split("/")[-1]
            pdf_response = requests.get(pdf_url)
            with open(f'pdfs/{pdf_name}', 'wb') as file:
                file.write(pdf_response.content)
            print(f"Downloaded {pdf_name}")
        except Exception as e:
            print(f"Error downloading PDF: {e}")

        # Go back to the main page
        driver.back()
        time.sleep(3)  # Wait for the main page to load



# Close the driver
driver.quit()
