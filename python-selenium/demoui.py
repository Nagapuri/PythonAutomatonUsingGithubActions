from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.chrome import ChromeType
from webdriver_manager.core.utils import ChromeType

# driver_path = ChromeDriverManager(ChromeType.CHROMIUM).install()
# driver = webdriver.Chrome(driver_path)
# service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# optional
chrome_options.add_argument('--no-sandbox')
# optional
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options,service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

# driver  = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
# driver = webdriver.Chrome(ChromeDriverManager(ChromeType.CHROMIUM).install())
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(options=chrome_options)
driver.get("https://google.com")
print(driver.title)

