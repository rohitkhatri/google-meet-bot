import time
import os
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-extensions")
# options.add_argument("--window-size=800,800")
# options.add_argument("--incognito")
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument(
    "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
user_data_dir = os.path.join(os.path.dirname(__file__), "browser/data")
options.add_argument(f"user-data-dir={user_data_dir}")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# )

# options.add_argument("--use-fake-ui-for-media-stream")
# options.add_argument("--window-size=1920x1080")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-setuid-sandbox")
# # options.add_argument('--headless=new')
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-application-cache")
# options.add_argument("--disable-setuid-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# options.add_argument(
#     "user-data-dir=/Users/rohitkhatri/Library/Application Support/Firefox/Profiles/1jaazq3l.default"
# )

driver = webdriver.Chrome(options=options)

driver.get("https://meet.google.com/isv-ivzz-ueg")

time.sleep(60 * 2)
