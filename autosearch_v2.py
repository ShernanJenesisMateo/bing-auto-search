from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
import os
import time
import subprocess

from places_to_search import places_to_search 

# Edge WebDriver path
edge_driver_path = r'C:\Users\smateo\Desktop\others\Playground\auto-search\msedgedriver.exe'

# User data directory
USER_DATA_DIR = "C:\\Users\\smateo\\AppData\\Local\\Microsoft\\Edge\\User Data"

# List of profile names
PROFILES = ["Profile 1", "Profile 2", "Profile 3", "Profile 4", "Profile 5"]

# Ensure the user data directory exists
if not os.path.exists(USER_DATA_DIR):
    print(f"User data directory does not exist: {USER_DATA_DIR}")
    exit()

# Set up the Edge driver service
service = EdgeService(edge_driver_path)

def sleep_with_message(sleepMessage, sleepTime):
    print("---------------------------" + sleepMessage.upper())
    time.sleep(sleepTime)

try:
    for PROFILE in PROFILES:
        # Ensure the profile directory exists
        profile_path = os.path.join(USER_DATA_DIR, PROFILE)
        if not os.path.exists(profile_path):
            print(f"Profile directory does not exist: {profile_path}")
            continue

        # Set up Edge options to use the specified profile
        options = Options()
        options.add_argument(f"user-data-dir={USER_DATA_DIR}")
        options.add_argument(f"profile-directory={PROFILE}")

        # Ensure no existing Edge processes are running
        subprocess.run(["taskkill", "/F", "/IM", "msedge.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Initialize the Edge WebDriver
        driver = webdriver.Edge(service=service, options=options)
        print("---------------------------Opening in existing browser session for profile:", PROFILE)
        
        # Adding a short delay after browser launch
        time.sleep(5)

        # Open Bing.com directly, assuming the profile is already logged in
        driver.get("https://www.bing.com/")
        print("---------------------------Opening Bing with profile:", PROFILE)

        # Wait for Bing homepage to load
        sleep_with_message("Bing homepage loading...", 5)

        for place in places_to_search:
            # Search for the input element by its ID
            sleep_with_message("Finding the search bar", 2)
            search_box = driver.find_element(By.ID, "sb_form_q")

            sleep_with_message("Preparing to type", 3)

            # Typing each character with a 1-second delay
            for char in place:
                search_box.send_keys(char)
                time.sleep(0.7)

            # Press Enter to submit the search
            search_box.send_keys(Keys.RETURN)

            # Wait for the search results
            print(f"Showing result of {place}")

            # Wait for the search results to load
            time.sleep(2)  # Adjust this delay as needed

            # Re-find the search box element
            sleep_with_message("Preparing to find the search bar again", 2)
            search_box = driver.find_element(By.ID, "sb_form_q")

            sleep_with_message("Preparing to clear search bar", 1)
            # Clear the search box
            search_box.clear()

        # Close the browser for this profile
        driver.quit()

    print("All profiles have finished searching.")

finally:
    # Close the browser if driver was instantiated
    if 'driver' in locals():
        driver.quit()
