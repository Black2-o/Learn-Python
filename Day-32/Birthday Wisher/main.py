
import random
import pandas
import datetime as dt
import smtplib
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


# My Email Password 
MYEMAIL = "noob125690@gmail.com"
MYPASS = "ojuqpvqzfnzmbddg"





# Select a Random Letter 
random_letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
with open(random_letter) as letter:
    letter = letter.read()
# Birthdays Time Get 
birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays.to_dict(orient="records")


# Now Time Get 
now = dt.datetime.now()

# Check That is there anybody's birthdays is today..... & Replace His/Her name and make final_letter and get his/her email address. 
for birthdaysDate in birthdays_dict:
    if now.day == birthdaysDate["day"] and now.month == birthdaysDate["month"]:
        send = birthdaysDate["name"]
        send_email = birthdaysDate["email"]
        final_letter = "Subject: Birthday wish\n\n" + letter.replace("[NAME]", send)
        # conncetion with Email and send Email
        with smtplib.SMTP("smtp.gmail.com", 587) as conncetion:
            conncetion.starttls()
            conncetion.login(user=MYEMAIL, password=MYPASS)
            conncetion.sendmail(from_addr=MYEMAIL,
            to_addrs=send_email,
            msg=final_letter)




