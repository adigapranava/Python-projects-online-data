from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\\Users\\Admin\\Desktop\\pranava\\python\\atomator\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_elements_by_id("productPrice" + str(i)) for i in range(1, -1, 1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
	actions.perform()
	try:
		count = int(cookie_count.text.split(" ")[0])
	except:
		count = 0
	for item in items:
		value = int(item.text)
		if value <= count:
			upgrade_actions = ActionChains(driver)
			upgrade_actions.move_to_element(item)
			upgrade_actions.click()
			upgrade_actions.perform()
	print(count)
	try:
		print("value-",value)
	except :
		pass

