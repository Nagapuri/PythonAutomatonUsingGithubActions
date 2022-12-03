from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType

driver_path = ChromeDriverManager(ChromeType.CHROMIUM).install()
driver = webdriver.Chrome(driver_path)

driver.get("https://google.com")

