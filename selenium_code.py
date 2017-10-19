from selenium import webdriver


driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get(base_url)
for i in range(10):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
pageSource = driver.page_source