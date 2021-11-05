# from google.cloud import bigquery
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

FIREFOX_BINARY = FirefoxBinary('/opt/firefox/firefox')
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
# options.add_argument("window-size=1920,1080")

# caps = webdriver.DesiredCapabilities().FIREFOX
# caps["marionette"] = True

def scrap_g2(url):
    # driver = webdriver.Firefox(firefox_binary=FIREFOX_BINARY, options = options)
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options = options)
    driver.get(url)
    time.sleep(3)
    driver.refresh()
    # driver.set_page_load_timeout(10)
    # try:
    #     WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, "div[@class='product-head product-head--banner']")))
    #     print ("Page is ready!")

    try:
        # star = driver.find_element_by_xpath("//meta[@itemprop='ratingValue']").get_attribute('content')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='star-wrapper d-f ai-c']")))
        star = driver.find_element_by_xpath("//meta[@name='twitter:data2']").get_attribute("value")
        elements = driver.find_element_by_css_selector("li[class='list--piped__li']").text
        review_count = elements.split()[0].replace(',','')
        print(f'Selenium Frank: *********scraping success*********at: {url}')
    except Exception as e:
        star = 0
        review_count = 0
        print(f'Selenium Frank: *********scraping fail*********{time.strftime("%Y-%m-%d %H:%M:%S")}: {url}')
        print("Exception: {}".format(type(e).__name__))
        print("Exception message: {}".format(e))

    # except Exception as e:
    #     print("Exception: {}".format(type(e).__name__))
    #     print("Exception message: {}".format(e)) 
    #     print("Loading took too much time!")
    # dropdown_loc = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]"
    # star_loc = "//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/span[1]
    # try:
        # dropdown = driver.find_element(By.XPATH, dropdown_loc)
        # achains = ActionChains(driver)
        # achains.move_to_element(dropdown).perform()
        # WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, star_loc)))
        # star = driver.find_element(By.XPATH, star_loc).text
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "is-hidden")))        
        # star = driver.find_element_by_xpath("//meta[@itemprop='ratingValue']").get_attribute('content')
        # # star = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/span[1]/meta[3]").get_attribute('content')
        # print(f'Selenium Frank: *********scraping star success*********: {url}')

    # except Exception as e: 
    #         star = 0  
    #         print(f'Selenium Frank: *********scraping star fail*********: {url}') 
    #         print("Exception: {}".format(type(e).__name__))
    #         print("Exception message: {}".format(e)) 

    driver.close()
    driver.quit()
    return int(review_count), float(star.split()[0])

# a, b = scrap_g2('https://www.g2.com/products/servicenow-now-platform/reviews')
# print(float(b.split()[0]))
# review, score = scrap_g2('https://www.g2.com/products/talkdesk/reviews')
# print(review, score)

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options = options)
# driver.get('https://www.g2.com/products/intercom/reviews')
# star = driver.find_element_by_xpath("//meta[@itemprop='ratingValue']").get_attribute('content')
# element = driver.find_element_by_css_selector("div[class='text-center ai-c star-wrapper__desc__rating']")
# element = element.find_element_by_css_selector("span[class='fw-semibold']")

# print(element.text)


 
    # review = element.split()[0].replace(',','')
# review
