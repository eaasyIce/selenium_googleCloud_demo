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
options.add_argument("window-size=1024,768")
options.add_argument("no-sandbox")
options.headless = True

# options.add_argument("--no-sandbox")

def scrap_gartner(url):
    driver = webdriver.Firefox(firefox_binary=FIREFOX_BINARY, options = options)
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options = options)
    # driver.implicitly_wait(5)
    driver.get(url)
    # driver.set_page_load_timeout(20)
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@class='logo-name-buttons-container']")))
        print ("Selenium Frank: Page element is ready!")

        try:
            star = element.find_elements_by_class_name("ratingNumber")[0].text
            review_count = element.find_elements_by_class_name("ratingLabel")[0].text
            review_count = review_count.split()[0]
            print(f'Selenium Frank: *********scraping success*********at: {url}')
        except Exception as e:
            star = 0
            review_count = 0
            print(f'Selenium Frank: *********scraping failed*********{time.strftime("%Y-%m-%d %H:%M:%S")}: {url}')
            print("Exception: {}".format(type(e).__name__))
            print("Exception message: {}".format(e))

    except Exception as e:
        print("Exception: {}".format(type(e).__name__))
        print("Exception message: {}".format(e)) 
        print("Selenium Frank: Loading took too much time!")
        
    # driver.close()
    driver.quit()
    return int(review_count), float(star)

# a, b = scrap_gartner('https://www.gartner.com/reviews/market/workforce-engagement-management/vendor/talkdesk/product/workforce-engagement-management-product-from-talkdesk')
# a, b = scrap_gartner('https://www.gartner.com/reviews/market/contact-center-as-a-service/vendor/talkdesk/product/talkdesk')
# print(a,b)

# print(type(b))
