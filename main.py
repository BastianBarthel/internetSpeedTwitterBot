import os
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

TWITTER_EMAIL = os.environ.get(TWITTER_EMAIL)
TWITTER_PASSWORD = os.environ.get(TWITTER_PASSWORD)
CHROME_DRIVER_PATH = "/Applications/chromedriver"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        agree_button = self.driver.find_element_by_css_selector("#_evidon-banner-acceptbutton")
        agree_button.click()
        go_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        )
        go_button.click()
        time.sleep(40)
        self.down = self.driver.find_element_by_css_selector(".download-speed").text
        self.up = self.driver.find_element_by_css_selector(".upload-speed").text

    def tweet_internet_speed(self):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/a[2]'
        )
        login_button.click()
        time.sleep(2)
        username_input = self.driver.find_element_by_name("session[username_or_email]")
        username_input.send_keys(TWITTER_EMAIL)
        password_input = self.driver.find_element_by_name("session[password]")
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet_input = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        )
        tweet = f"Download: {self.down} Mbit/s, Upload: {self.up} Mbit/s"
        tweet_input.send_keys(tweet)
        time.sleep(2)
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]'
        )
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_internet_speed()
