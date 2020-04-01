import datetime
import unicodecsv as csv
import xlsxwriter
import math
import time
import xlrd
from selenium  import webdriver
from time      import sleep
import xlwt 
from xlwt import Workbook
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import os

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Product Name')
sheet1.write(0, 1, 'Was Price')
sheet1.write(0, 2, 'Current Price')
sheet1.write(0, 3, 'Image Url')
sheet1.write(0, 4, 'Discount')
wb.save('result.xls')

url = 'https://diaonline.supermercadosdia.com.ar/bebidas/aguas/aguas-con-gas'

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)

# chrome_options = Options() 
# chrome_options.add_argument("--headless")  
# driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options)
driver.get(url)

# amount = driver.find_element_by_xpath('//*[@id="appVue"]/div[2]/section/div/div/div[2]/div/div/p[1]/span[1]').text
# amount = amount.split(':')[1].replace(' ','')
# print(amount)
# print('------')
# page = int((int(amount) - int(amount)%16)/16 + 1)
# print(page)

scroll_pause_time = 2
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	sleep(scroll_pause_time)
	new_height = driver.execute_script('return document.body.scrollHeight')

	if new_height == last_height:
		try:
			driver.find_element_by_class_name('cargarMas').click()
			sleep(scroll_pause_time)
		except:
			break
	last_height = new_height


link_array = []

sliders = driver.find_elements_by_class_name('slider__slide')
for slider in sliders:
    link = slider.find_element_by_class_name('productImage').get_attribute('href')
    link_array.append(link)
    print(link)
print(len(link_array),"--")

# //*[@id="ResultItems_3419720"]/div[13]/ul[4]/li[4]/div/div/div/div[1]/figure/a/img


sleep(3)
driver.quit()










