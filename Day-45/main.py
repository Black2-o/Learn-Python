from bs4 import BeautifulSoup

# import lxml

with open("website.html",encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.text)
# print(soup.a)
# all_anchor_tag=soup.find_all(name="a")
# print(all_anchor_tag)

# for tag in all_anchor_tag:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find_all(name="h3", class_="heading")
# print(section_heading)

# for heading in section_heading:
#     print(heading.get("class"))

company_url  = soup.select_one(selector="p a")
print(company_url)