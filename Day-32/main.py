# import smtplib

my_email = "noob125690@gmail.com"
password = "ojuqpvqzfnzmbddg"

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#     to_addrs="black2.o@yahoo.com",
#     msg="Subject:Hello Python!\n\nHey This is made by Python")





# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day

# day_of_weak = now.weekday() + 1

# if year == 2023:
#     print("This is 2023")

# print(day_of_weak)

# my_date_of_birth = dt.datetime(year=2007, month=7, day=23, hour=00)
# print(my_date_of_birth)


import datetime as dt
import random
import smtplib

# Work With Time 
now = dt.datetime.now()
day_of_weak = now.weekday() +1
minute = now.minute
print(minute)
# email_sending_time = dt.datetime(year=2023, month=8, day=5, hour=00, minute=11)
# email_sending_time_minute = email_sending_time.minute


# Work With File
with open("quotes.txt") as text:
    quotes = text.readlines()
    quotes_no = random.randint(0, len(quotes) - 1)
    final_quotes = quotes[quotes_no]
    
if day_of_weak == 6:
    #work with Email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
        to_addrs="black2.o@yahoo.com",
        msg=f"Subject:Daily Quotes!\n\n{final_quotes}")