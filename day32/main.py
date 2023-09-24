# import smtplib

# my_email = "test@gmail.com"
# password = "abcd1234()"
# friends_email = "friend@gmail.com"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=friends_email, msg="Hello")

import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

print(year, month, day, day_of_week)
if year == 2023: 
    print("Hello!")

date_of_birth = dt.datetime(year=1995, month=12 , day=15, hour=4 )