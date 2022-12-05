from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.chrome import ChromeType
from webdriver_manager.core.utils import ChromeType
from chromedriver_py import binary_path

service_object = Service(binary_path)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# optional
# chrome_options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome(service=service_object)

driver.get("https://google.com")
print(driver.title)

