from InternetSpeed import InternetSpeed
from Twitter import Twitter

internet_reading = InternetSpeed()
readings = internet_reading.getSpeedReadings()
print(readings)

user = Twitter()
user.sign_in()

user.check_for_internet_speed_and_make_a_complaint_if_low_down_or_up(readings_of_internet_speed_test=readings)