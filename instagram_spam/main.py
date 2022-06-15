from selenium import webdriver
from instagramuser import username, password
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



class instagram():
    def __init__(self,username,password,aranacak_kisi):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.aranacak_kisi = aranacak_kisi

    def signIn(self):
        
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username_input = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        password_input = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)       
        
        simdi_degil = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()      
        time.sleep(4)
        bildirim_simdi_degil = self.browser.find_element_by_css_selector("button.aOOlW:nth-child(2)").click()
        time.sleep(2)
        ara = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(self.aranacak_kisi)
        time.sleep(2)
        # bul = self.browser.find_element_by_xpath("//*[@id='f717b704dc3784']/div/div/div").send_keys(Keys.ENTER)
        clickd = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        clickd.send_keys(Keys.ENTER)
        clickd.send_keys(Keys.ENTER)
        # time.sleep(1)
        # ara.send_keys(Keys.ENTER)
        time.sleep(4)
        span = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div/button").click()
        time.sleep(2)
        ban = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div/button[3]").click()
        time.sleep(2)
        neden_secimi = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div/div[1]").click()
        time.sleep(2)
        secenek = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[1]").click()
        time.sleep(1)
        
        spann = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[1]").click()
        time.sleep(1)
        
        


insta = instagram(username,password,aranacak_kisi="")
insta.signIn()
