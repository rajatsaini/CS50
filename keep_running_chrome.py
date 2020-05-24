from selenium import webdriver
import time


while True:
	driver = webdriver.Chrome()
	url = "https://www.youtube.com/watch?v=-Psuvub6Yek"
	
	driver.get(url)
	driver.implicitly_wait(20)
	driver.switch_to.frame(0)

	try :
		element = driver.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']")
		element.click()
		time.sleep(250)
		driver.quit()
		time.sleep(1)
	except:
		print("I ran into Exception")
		driver.quit()
