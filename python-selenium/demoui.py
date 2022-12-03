from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.chrome import ChromeType
from webdriver_manager.core.utils import ChromeType

driver_path = ChromeDriverManager(ChromeType.CHROMIUM).install()
driver = webdriver.Chrome(driver_path)

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get("https://google.com")

