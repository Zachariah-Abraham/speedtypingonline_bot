from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')
driver.get('https://www.speedtypingonline.com/typing-test')
        
for j in range(1, 10000000):
    for i in range(0, 4):
        for k in range(1, 1000): 
            try:
               toSend = driver.find_element_by_xpath('//*[@id="blockLine'+str(i)+'"]/span['+str(k)+']').text
            except NoSuchElementException:
                break

            if(toSend == '&nbsp;'):
                toSend = ' '
            actions = ActionChains(driver)
            actions.send_keys(toSend)
            actions.perform()
    
