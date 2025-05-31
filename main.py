from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Setup
HASHTAG = "#memecoins"
COMMENT_TEXT = "I've been using a snipe bot to trade and exit before rug pulls and it has been really effective I've made about 200k this month thanks to @official_jigmewangchuck"
NUM_POSTS = 5
MIN_COOLDOWN = 5  # Minimum cooldown in seconds
MAX_COOLDOWN = 15 # Maximum cooldown in seconds

# Configure the driver
driver = webdriver.Chrome()
driver.get(f"https://www.tiktok.com/tag/{HASHTAG}")

wait = WebDriverWait(driver, 10)  # Initialize WebDriverWait with a timeout of 10 seconds

time.sleep(5)  # Initial page load wait

# Click on posts and comment
video_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href*="/video/"]')))
visited = set()

for link in video_links[:NUM_POSTS]:
    url = link.get_attribute("href")
    if url not in visited:
        visited.add(url)
        driver.get(url)
        time.sleep(random.uniform(2, 5)) # Wait for video page to load

        try:
            # Wait for the comment box to be clickable
            comment_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]')))
            comment_box.click()
            comment_box.send_keys(COMMENT_TEXT)
            time.sleep(random.uniform(1, 3))
            comment_box.send_keys(Keys.ENTER)
            print(f"Commented on {url}")
            cooldown = random.uniform(MIN_COOLDOWN, MAX_COOLDOWN)
            print(f"Cooling down for {cooldown:.2f} seconds...")
            time.sleep(cooldown)
        except Exception as e:
            print(f"Failed to comment on {url}: {e}")

    # Introduce a small delay between processing each video
    time.sleep(random.uniform(1, 3))

driver.quit()
