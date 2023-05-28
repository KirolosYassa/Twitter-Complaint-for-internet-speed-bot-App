import os
from dotenv import load_dotenv
from InternetSpeed import InternetSpeed
import time

# user = LinkedIn(url="https://www.linkedin.com/jobs/search/?currentJobId=3602007740&f_AL=true&geoId=102007122&keywords=python%20developer&location=Cairo%2C%20Egypt&refresh=true")


# user.signin()
# job_list = user.get_jobs_list()

internet_reading = InternetSpeed()
readings = internet_reading.getSpeedReadings()
print(readings)
