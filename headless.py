from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
chrome_options.binary_location ="/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary"
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://www.baidu.com')
print(driver.page_source)