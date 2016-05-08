from selenium import webdriver
from selenium.webdriver.common.keys import Keys

routerIP = '192.168.1.1'
VPNpage = 'http://' + routerIP + '/Advanced_OpenVPNClient_Content.asp' #ASUS merlin firmware ONLY

#you must first download the ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/home and specify it in the parameters below like so: Chrome("l:/ocation/of/driver/")
browser = webdriver.Chrome("ADD YOUR CHROMEDRIVER LOCATION HERE") #You can use whichever browser you want, just be sure to make sure you have the correct driver mentioned above (look at the documentation or change the browser on this line and execute, you will be given the link by the debugger)
browser.get(VPNpage)

userLogin = browser.find_element_by_name('login_username')
passLogin = browser.find_element_by_name('login_passwd')

userLogin.send_keys('myUsername') #your router firmware username
passLogin.send_keys('myPassword') #your router firmware password
browser.execute_script('login();')

browser.find_element_by_class_name('iphone_switch').click()
