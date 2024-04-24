from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# title
print(soup.title)

# all anchor tags
all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

heading = soup.find(name='h1',id='name')
print(heading)

section_heading = soup.find(name='h3', class_="heading")
print(section_heading.getText())

# css selector
name = soup.select_one("#name")
company_url = soup.select_one(selector="p a")
print(company_url)