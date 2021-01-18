from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep


class InternetSpeedTwitterBot():
    chrome_driver_path = "C:\\Users\\marce\\Downloads\\chromedriver_win32\\chromedriver.exe"
    TWITTER_EMAIL = '--'
    TWITTER_PASSWORD = '--'
    PROMESED_DOWN = 120
    PROMESED_UP = 20
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.down = 0
        self.up = 0
        self.resultId = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.goButton = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.goButton.click()
        sleep(50)
        self.down =self.driver.find_element_by_css_selector(".download-speed").text
        self.up =self.driver.find_element_by_css_selector(".upload-speed").text
        self.resultId = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a').text

    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com/")
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span').click()
        sleep(1)
        self.username = self.driver.find_element_by_name("session[username_or_email]")
        self.username.send_keys(self.TWITTER_EMAIL)
        self.password = self.driver.find_element_by_name("session[password]")
        self.password.send_keys(self.TWITTER_PASSWORD)
        self.password.send_keys(Keys.ENTER)
        sleep(3)
        self.twitter = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        self.twitter.send_keys(f"hey Internet Provider, why my internet speed {self.down}dwn/{self.up}up when i pay for {self.PROMESED_DOWN}dwn/{self.PROMESED_UP}up?")
        self.twitterButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span')
        self.twitterButton.click()

        