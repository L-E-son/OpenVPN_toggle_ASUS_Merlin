from selenium import webdriver
from selenium.webdriver.common.keys import Keys

routerIP = '192.168.1.1'
VPNpage = 'http://' + routerIP + '/Advanced_OpenVPNClient_Content.asp' #ASUS merlin firmware ONLY

#you must first download the ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/home and specify it in the parameters below like so: Chrome("l:/ocation/of/driver/")
browser = webdriver.Chrome("") #You can use whichever browser you want, just be sure to make sure you have the correct driver mentioned above (look at the documentation or change the browser on this line and execute, you will be given the link)
browser.get(VPNpage)

userLogin = browser.find_element_by_name('login_username')
passLogin = browser.find_element_by_name('login_passwd')

userLogin.send_keys('myUsername')
passLogin.send_keys('myPassword')
browser.execute_script('login();')

browser.find_element_by_class_name('iphone_switch').click()