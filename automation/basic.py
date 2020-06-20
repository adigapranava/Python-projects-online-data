from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Process of pressing 'enter'
import  time
# this is used to wait till the page is loaded
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\\Users\\Admin\\Desktop\\pranava\\python\\atomator\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:  #this will wait for browser to load the page for 10 sec
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()
    driver.back()
    driver.back()
    driver.back()
    driver.forward()
finally:
    driver.quit()

time.sleep(5)
driver.quit()
