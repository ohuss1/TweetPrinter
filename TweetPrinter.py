from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import bs4
import string
driver=webdriver.Firefox(executable_path=r'C:\Users\OComp\Desktop\geckodriver-v0.23.0-win64\geckodriver.exe'
                         )#replace the path with your gecko exe path
print('Please enter the twitter url')
UrlString=raw_input()
#print(UrlString)
driver.get(UrlString)
time.sleep(1)
numpages=3;
print('please enter number of pages you would like to print')
numpages=(int(raw_input()))
#print(numpages)
#print(type(numpages))
