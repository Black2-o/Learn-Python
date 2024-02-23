from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com/news"

response = requests.get(URL)

# print(response.text)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# print(soup.title)

title_list_with_ancher_tag = soup.select(".titleline a")
# print(title_list_with_ancher_tag)
article_upvote = soup.select(".score")

serial_no = 1
for single_title in title_list_with_ancher_tag:
    if len(article_upvote) > serial_no:
        print(str(serial_no) + "  " +single_title.text)
        print("     Link: "+ single_title.get("href"))
        # for score in article_upvote:
        #     if serial_no+1 == 
        #         upvote = ("     UPvote: "+ score.text)
        upvote = article_upvote[serial_no]
        print("     UPvote: "+ upvote.text)

    serial_no += 1