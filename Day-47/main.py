from bs4 import BeautifulSoup
import requests
import smtplib

PRODUCT_URL = "https://www.amazon.com/Gaming-Keyboard-Mouse-Combo-Mechanical/dp/B09X23WTHX/ref=sr_1_4?crid=3KNH34UD3ICKK&keywords=white+keyboard+and+mouse+wireless+combo+rgb&qid=1694095116&sprefix=white+keyboard+and+mouse+wireless+combo+rgb%2Caps%2C626&sr=8-4"

HEADERS = { 'Accept-Language' : "en-US,en;q=0.9",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0"}
MY_EMAIL = "noob125690@gmail.com"
MY_PASS = "ojuqpvqzfnzmbddg"



response = requests.get(PRODUCT_URL, headers=HEADERS)

code_all = response.text

soup = BeautifulSoup(code_all, "html.parser")

# print(soup)

rate_in_string = (soup.select(".a-offscreen")[1]).text
# rate = soup.select("tr td span span")

rate = rate_in_string

txt = "hello, my name is Peter, I am 26 years old"

rate = float(rate_in_string.split("$")[1])

# print(float(rate))

if rate < 150:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
        to_addrs="black2.o@yahoo.com",
        msg= "Subject:Product to Buy\n\nHey Your 'Gaming Keyboard and Mouse Combo - Glorious GMMK 87% Percent Backlit RGB TKL Mechanical Keyboard (White Ice) + Model O Wireless Gaming RGB Matte White Mouse' This Product is less than 100. It's Your target Price. So you can buy this now.")




