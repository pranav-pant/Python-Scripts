from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://youtube.com")

searchbar = driver.find_element_by_xpath('//*[@id="search"]')
searchbar.send_keys("Marques Brownlee")

searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbutton.click()
