import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InternetSpeed():
    def __init__(self):
        load_dotenv()   
        self.url = "https://www.speedtest.net/"
        self.chrome_local_path = "C:\Development"
        self.driver = webdriver.Chrome(executable_path=self.chrome_local_path)
        self.driver.get(self.url)
        self.readings_of_internet_test_speed = {"COMPANY": "",
                                                "DOWNLOAD":0,
                                                "UPLOAD": 0,}
        
    def getSpeedReadings(self):
        self.start_internet_test()
        self.get_internet_test_speed_data()
        return self.readings_of_internet_test_speed
        
                
    def start_internet_test(self):
        go_test_button = self.driver.find_element(By.CLASS_NAME, 'js-start-test')
        go_test_button.click()
        time.sleep(50.2)
        
    def get_internet_test_speed_data(self):
        company = self.driver.find_element(By.CLASS_NAME, 'js-data-isp')
        company = company.text
        download = self.driver.find_element(By.CLASS_NAME, 'download-speed')
        download = download.text
        upload = self.driver.find_element(By.CLASS_NAME, 'upload-speed')
        upload = upload.text
        self.readings_of_internet_test_speed = {"COMPANY": company,
                                                "DOWNLOAD": download,
                                                "UPLOAD":upload}
        