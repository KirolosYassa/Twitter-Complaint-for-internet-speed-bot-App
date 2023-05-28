import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Twitter():                
    def __init__(self):
        load_dotenv()   
        self.email = os.getenv("EMAIL")
        self.username = os.getenv("TWITTER_USERNAME")
        self.password = os.getenv("PASSWORD")
        
        self.promise_download = os.getenv("PROMISED_DOWNLOAD")
        self.promise_upload = os.getenv("PROMISED_UPLOAD")
        
        self.url = "https://twitter.com/"
        self.chrome_local_path = "C:\Development"
        self.driver = webdriver.Chrome(executable_path=self.chrome_local_path)
        self.driver.get(self.url)
        
        self.readings_of_internet_speed_test = {}

    def sign_in(self):
        log_in = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a')
        log_in.click()
        time.sleep(2.1)
        
        fill_username = self.driver.find_element(By.NAME, "text")
        fill_username.send_keys(self.username)
        
        next_action = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_action.click()
        
        time.sleep(2.2)
        
        fill_password = self.driver.find_element(By.NAME, "password")
        fill_password.send_keys(self.password)


        log_in_in_form = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        log_in_in_form.click()
        time.sleep(5.2)
        
    
    def check_for_internet_speed_and_make_a_complaint_if_low_down_or_up(self, readings_of_internet_speed_test: dict):
        self.readings_of_internet_speed_test = readings_of_internet_speed_test
        if self.check_download_is_low() or self.check_upload_is_low():
            self.make_a_complaint()
            
            
    def check_download_is_low(self):
        return self.readings_of_internet_speed_test["DOWNLOAD"] < self.promise_download
    
    
    def check_upload_is_low(self):
        return self.readings_of_internet_speed_test["UPLOAD"] < self.promise_upload
    
    
    def make_a_complaint(self):
        company_name = self.readings_of_internet_speed_test["COMPANY"]
        download = self.readings_of_internet_speed_test["DOWNLOAD"]
        upload = self.readings_of_internet_speed_test["UPLOAD"]
        
        tweet_content = f"Hey @{company_name}, why is my internet speed {download}down/{upload}up when I pay for {self.promise_download}down/{self.promise_upload}up"
        
        tweet_space = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        tweet_space.send_keys(tweet_content)
        
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()
    