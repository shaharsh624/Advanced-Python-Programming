from bs4 import BeautifulSoup

with open("UNIT 3\Assignment\scrap.html", "r") as htmlfile:
    content = htmlfile.read()

soup = BeautifulSoup(content, "html.parser")

title = soup.title
print("Title: ", title.text)

heading = soup.h1
print("Heading: ", heading.text)

paragraphs = soup.find_all("p")
print("Paragraphs: ")
for paragraph in paragraphs:
    print(paragraph.text)

lists = soup.find_all("li")
print("Lists: ")
for list in lists:
    print(list.text)

print()
print("New HTML File")
print()

new_list = soup.new_tag("li")
new_list.string = "List-4"
ol = soup.ol
ol.append(new_list)

lists = soup.find_all("li")
print("Lists: ")
for list in lists:
    print(list.text)

div = soup.new_tag("div")
div.string = "Now creating a division element in the webpage."
body = soup.body
body.append(div)
print(div.text)

with open(r"UNIT 3\Assignment\scrap.html", "w") as htmlfile:
    htmlfile.write(soup.prettify())
