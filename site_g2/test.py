# from google.cloud import bigquery
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

import browser_cookie3
cookies = browser_cookie3.chrome(domain_name='.g2.com')
    
# FIREFOX_BINARY = FirefoxBinary('/opt/firefox/firefox')
options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.headless = True

# options.add_argument("window-size=1920,1080")

# caps = webdriver.DesiredCapabilities().FIREFOX
# caps["marionette"] = True


driver = webdriver.Chrome(executable_path=r"C:\Users\fjia\Downloads\chromedriver_win32\chromedriver.exe", options = options)

    
# driver.set_window_size(1920, 1080)
# driver.set_page_load_timeout(10)
driver.get('https://www.g2.com/products/servicenow-now-platform/reviews')
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
time.sleep(3)
driver.refresh()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='star-wrapper d-f ai-c']")))

# driver.get('https://www.g2.com/products/genesys-cloud-cx/reviews')
# star = driver.find_element_by_css_selector
star = driver.find_element_by_xpath("//meta[@name='twitter:data2']").get_attribute("value")
# print(stars)
driver.close()
driver.quit()
print(star)
# star = star.split()[0]
# print(star)
# dropdown = driver.find_element_by_css_selector('.star-wrapper.d-f.ai-c')

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='star-wrapper d-f ai-c']")))
# dropdown = driver.find_element('.show-for-xlarge.d-f.ai-c')
# dropdown = driver.find_element_by_css_selector('.show-for-xlarge.d-f.ai-c')
# achains = ActionChains(driver)
# achains.move_to_element(dropdown).perform()
# starEl = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".show-for-xlarge.d-f.ai-c.hover")))
# star = starEl.find_element(By.CSS_SELECTOR, star_loc).text
driver.close()
driver.quit()


# dropdown_loc = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]"
# star_loc = "body.rebrand.js.x-user-login-status-initialized.media-slim.media-regular.is-linked-out.is-logged-out:nth-child(2) div.off-canvas-wrapper:nth-child(2) div.off-canvas-wrapper-inner div.off-canvas-content div.d-f.fd-c.full-view-min-height:nth-child(2) div.f-1.fb-a div.page:nth-child(2) div.product-head.product-head--banner div.product-head__title__wrap div.product-head__title div.star-wrapper.d-f.ai-c div.show-for-xlarge.d-f.ai-c div.dropdown-box.dropdown-box--arrow__north div.text-small.my-half div.text-center.ai-c.star-wrapper__desc__rating > span.fw-semibold:nth-child(1)"
   
# elements = driver.find_element_by_css_selector("li[class='list--piped__li']").text
# review_count = elements.split()[0].replace(',','')

# print(star)


    # except Exception as e:
    #     print("Exception: {}".format(type(e).__name__))
    #     print("Exception message: {}".format(e)) 
    #     print("Loading took too much time!")

    # try:

        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "is-hidden")))        
        # star = driver.find_element_by_xpath("//meta[@itemprop='ratingValue']").get_attribute('content')
        # # star = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/span[1]/meta[3]").get_attribute('content')
        # print(f'Selenium Frank: *********scraping star success*********: {url}')

    # except Exception as e: 
    #         star = 0  
    #         print(f'Selenium Frank: *********scraping star fail*********: {url}') 
    #         print("Exception: {}".format(type(e).__name__))
    #         print("Exception message: {}".format(e)) 


