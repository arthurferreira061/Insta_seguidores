from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
from pynput.keyboard import Key, Controller
from random import *

keyboard = Controller()


chromedriver_path = 'C:/Users/gabri/Downloads/bot/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('YOUR_USER')
password = webdriver.find_element_by_name('password')
password.send_keys('YOUR_PASSWORD')
sleep(3)

button_login = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button')
button_login.click()
sleep(4)

# sleep(4)
# notnow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
# notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications
sleep(3)

search = webdriver.find_element_by_class_name('coreSpriteSearchIcon')
search.click()
sleep(3)

search_word = webdriver.find_element_by_css_selector('#react-root > section > nav > div:nth-child(2) > div > div > div:nth-child(2) > input')
search_word.send_keys('@INSTAPOPULAR')
sleep(2)
keyboard.press(Key.enter)
sleep(1)
keyboard.press(Key.enter)
sleep(2)

following = webdriver.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(3) > a[href*='/popugramsg/following/']")
following.click()
sleep(2)

j = 1
while j <= 4:
    keyboard.press(Key.tab)
    sleep(0.5)
    j += 1

k = 1
while k <= 6:
    keyboard.press(Key.down)
    sleep(0.5)
    k += 1

j = 1
while j <= 4:
    keyboard.press(Key.tab)
    sleep(0.5)
    j += 1

k = 1
while k <= 352:
    keyboard.press(Key.down)
    sleep(0.2)
    k += 1

sleep(4)

# y = 1
while True:
    # y += 1
    i= 1
    while i <= 175:
        try:
            timeFollow = randrange(5, 60)
            sleep(timeFollow)
            follow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[' + str(i) + ']/div/div[2]/button')
            follow.click()
        
        except:
            sleep(4)
            cancel = webdriver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            cancel.click()
            i = i - 1
            
        i = i + 1
        
    prox = randrange(5, 120)
    sleep(prox)

    i = 1 
    while i <= 175:
        
        timeUnfollow = randrange(5, 60)
        follow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[' + str(i) + ']/div/div[2]/button')
        follow.click()
        sleep(4)
        try:
            confirm = webdriver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
            confirm.click()
            sleep(timeUnfollow)
            i += 1

        except:
            i += 1

    sleep(prox)
