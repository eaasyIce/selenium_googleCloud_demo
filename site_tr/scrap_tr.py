from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

FIREFOX_BINARY = FirefoxBinary('/opt/firefox/firefox')
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("window-size=1024,768")
options.headless = True
# caps = webdriver.DesiredCapabilities().FIREFOX
# caps["marionette"] = True

def scrap_tr(url):
    driver = webdriver.Firefox( firefox_binary=FIREFOX_BINARY, options = options)
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options = options)

    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ProductHeader_main-content__1U1qp")))
        print ("Selenium Frank: Page is ready!")
        try:
            star = driver.find_element_by_xpath("//span[@itemprop='ratingValue']").text
            review_count = driver.find_element_by_xpath("//div[@class='ProductReviews_pager__1k8H7']").text
            review_count = review_count.split(" ")[-1][:-1]
            print(f'Selenium Frank: *********scraping success*********at: {url}')
        except Exception as e:
            star = 0
            review_count = 0
            print(f'Selenium Frank: *********scraping failed*********{time.strftime("%Y-%m-%d %H:%M:%S")}: {url}')
            print("Exception: {}".format(type(e).__name__))
            print("Exception message: {}".format(e))    

        print(f'Selenium Frank: the scraping of {url} is completed')
    except Exception as e:
        print("Exception: {}".format(type(e).__name__))
        print("Exception message: {}".format(e)) 
        print("Selenium Frank: Loading took too much time!")
    # driver.close()
    driver.quit()      
    return int(review_count), float(star)
