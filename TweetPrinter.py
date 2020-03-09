from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import bs4
import string
driver=webdriver.Firefox(executable_path=r'INSERT YOUR GECKO DRIVER PATH HERE'
                         )#replace the path with your gecko exe path
print('Please enter the emailid of facebook')
email=raw_input()
print('Please enter the password of facebook')
password=raw_input()
#print(UrlString)
driver.get("https://www.facebook.com/")
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
time.sleep(1)
driver.find_element_by_id('loginbutton').click()

#print(UrlString)
#driver.get(UrlString)
numpages=3;
#print('please enter number of pages you would like to print')
#numpages=(int(raw_input()))
#print(numpages)
#print(type(numpages))
time.sleep(3)
body=driver.find_element_by_tag_name('body')
for i in range(numpages):
	print(i)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(3)
#have scrolled down so numpages of pages loaded
postsfb = driver.find_elements_by_class_name('_5pcr.userContentWrapper')


for x in range(len(postsfb)): 
     textP=postsfb[x].find_element_by_tag_name('p')
     print(textP.text)
#file=open("Tweetss.txt","wb+")
#for tweet in tweets:
 #   x=tweet.text 
  #  x=x.encode('ascii',errors='ignore')
   # file.write(x)#to create a text file with tweets
    #file.write(('\n').encode())
   # file.write(('\n').encode())
#file.write(('end of scanned tweets').encode())
print('end')
#file.close()
