from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)   # 注意，这里如果找不到，请写你的驱动路径在参数里
#driver = webdriver.Chrome()
driver.get('https://google.com/')
driver.close()