import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

web_driver = ""


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()

        go_button = self.driver.find_element(By.CSS_SELECTOR, ".js-start-test")
        go_button.click()
        print("clicked!")

        time.sleep(60)

        self.up = float(self.driver.find_element(By.CSS_SELECTOR, "span.download-speed").text)
        self.down = float(self.driver.find_element(By.CSS_SELECTOR, "span.upload-speed").text)
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com/login")
        print("navigated to twitter now")

        time.sleep(15)

        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        print("email entered.")

        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span')
        next_button.click()
        time.sleep(3)
        print("next button clicked.")

        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        print("logged in.")

        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        print("tweet composed.")
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()
        print("tweeted!")

        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(web_driver)
bot.get_internet_speed()
bot.tweet_at_provider()
