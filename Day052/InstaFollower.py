from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep


class InstaFollower():
    chrome_driver_path = "C:\\Users\\marce\\Downloads\\chromedriver_win32\\chromedriver.exe"
    
    USER = '-'
    PW = '-'

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)


    def login(self):
        self.driver.get("https://www.instagram.com")
        sleep(2)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(self.USER)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(self.PW)
        sleep(2)
        password.send_keys(Keys.ENTER)
        
        

    def find_followers(self):
        sleep(5)
        self.driver.get("https://www.instagram.com/soucintiagomes")
        sleep(2)
        link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        link.click()
        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()