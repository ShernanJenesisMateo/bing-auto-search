from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import time

# Edge WebDriver path
edge_driver_path = r'C:\Users\smateo\Desktop\others\Playground\auto-search\msedgedriver.exe'

# Set up the Edge driver service
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

def sleep_with_countdown(seconds, message):
    for remaining in range(seconds, 0, -1):
        if remaining == 10:
            print("---------------------------" + message.upper())
        time.sleep(1)

def sleep_with_message(sleepMessage, sleepTime):
    print("---------------------------" + sleepMessage.upper())
    time.sleep(sleepTime)

try:
    # Open the Microsoft login page
    driver.get('https://login.live.com/')
    print("---------------------------sign in process ongoing")

    # Wait 60 seconds for login, print message 10 seconds before ending
    sleep_with_countdown(30, "---------------------------Sign in process ends in 10 secs")

    # Open a new tab
    sleep_with_message("preparing to open a new tab", 5)
    driver.execute_script("window.open('');")

    # Switch to the newly opened tab
    sleep_with_message("preparing to switch tab", 5)
    driver.switch_to.window(driver.window_handles[1])

    # Wait for the switch to complete
    sleep_with_message("waiting for tab switch", 5)

    # Navigate to Bing.com
    sleep_with_message("preparing to navigate to bing.com", 5)
    driver.get("https://www.bing.com/")

    # Wait for Bing homepage to load
    sleep_with_message("Bing homepage loading...", 10)

    places_to_search = [
    "tokyo japan", 
    "manila philippines", 
    "paris france",
    "new york usa",
    "sydney australia",
    "cape town south africa",
    "london uk",
    "rio de janeiro brazil",
    "beijing china",
    "rome italy",
    "moscow russia",
    "dubai uae",
    "toronto canada"
]
  # Add more places here

    for place in places_to_search:
        # Search for the input element by its ID
        sleep_with_message("finding the search bar", 2)
        search_box = driver.find_element(By.ID, "sb_form_q")

        sleep_with_message("preparing to type", 1)

        # Typing each character with a 1-second delay
        for char in place:
            search_box.send_keys(char)
            time.sleep(0.7)

        # Press Enter to submit the search
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results
        print(f"showing result of {place}")

        # Wait for the search results to load
        time.sleep(2)  # Adjust this delay as needed

        # Re-find the search box element
        sleep_with_message("preparing to find the search bar again", 2)
        search_box = driver.find_element(By.ID, "sb_form_q")

        sleep_with_message("preparing to clear search bar", 1)
        # Clear the search box
        search_box.clear()

    # Wait 20 seconds to see the search results, print message 10 seconds before ending
    sleep_with_countdown(15, "Program will end in 10 secs")

finally:
    # Close the browser
    driver.quit()
