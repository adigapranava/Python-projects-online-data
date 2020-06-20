from selenium import webdriver
PATH = "C:\\Users\\Admin\\Desktop\\pranava\\python\\atomator\\chromedriver.exe"
driver =  webdriver.Chrome(PATH)
driver.get("https://www.jiosaavn.com/")

playlist = driver.find_element_by_xpath('//*[@id="top-15"]/div[1]/ol')
playlists = playlist.find_elements_by_tag_name('li')

for count,item in enumerate(playlists,1):
	print(count,item.find_element_by_tag_name("h3").text)
	print("	",item.find_element_by_tag_name('span').text)
	print("	",item.find_element_by_tag_name('cite').text,"\n")
© 2020 GitHub, Inc.
