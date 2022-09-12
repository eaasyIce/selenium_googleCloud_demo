# from google.cloud import bigquery
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Option
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def crawler(url_list:list[str]) ->list[tuple]:
    firefox_options = FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument("--disable-gpu")
    firefox_options.add_argument("--no-sandbox")
    firefox_options.add_argument("window-size=1024,768")
    
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options = firefox_options)
    results = []
    for url in url_list:
        star = -1
        rating = -1
        try:
            driver.get(url)
            time.sleep(3)
            star = driver.find_element(By.CLASS_NAME,"ratingNumber").text
            rating = driver.find_element(By.CLASS_NAME,"ratingLabel").text.split(" ")[0]# print(stars)
        except:
            print(f'******* Crawler: fail to crawl: {url} *******')
            continue
        results.append((star, rating))
    driver.close()
    driver.quit()
    return results

# test = ["https://www.gartner.com/reviews/market/crm-customer-engagement-center/vendor/zendesk/product/zendesk-suite/reviews",
# "https://www.gartner.com/reviews/market/crm-customer-engagement-center/vendor/salesforce/product/salesforce-center-cloud/reviews"]

# print(crawler(test))