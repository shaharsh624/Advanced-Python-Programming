from bs4 import BeautifulSoup

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heading Tag</title>
</head>
<body>
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <h4>Heading 4</h4>
    <h5>Heading 5</h5>
    <h6>Heading 6</h6>
    <hr>

    <!-- comment -->

    <p>
        This is a p tag <br>

        Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime, voluptas aspernatur hic velit molestias repudiandae consectetur enim necessitatibus doloremque rerum aliquid facilis esse vel incidunt optio ea temporibus dolorem cum.
    </p><hr>

    <a href="https://www.google.com" target="_blank">Google</a>

    <br><br>

    <img src="https://images.alphacoders.com/112/112121.jpg" alt="wallpaper" height="300px">

    <a href="https://images.alphacoders.com/112/112121.jpg" target="_blank">
        <img src="https://images.alphacoders.com/112/112121.jpg" alt="wallpaper" height="300px">
    </a>

    <h3>List</h3>

    <ul type="circle">
        <li>google</li>
        <li>microsoft</li>
        <li>intel</li>
        <li>samsuung</li>
    </ul>

    <ol type="1" start="5">
        <li>google</li>
        <li>microsoft</li>
        <li>intel</li>
        <li>samsuung</li>
    </ol>
</body>
</html>
"""

# Parsing the HTML code
soup = BeautifulSoup(html_code, "html.parser")

# Extract and print the text within each heading tag (h1 to h6)
for i in range(1, 7):
    heading = soup.find("h{}".format(i))
    if heading:
        print(f"Heading {i}: {heading.text}")

# Extract and print the text within the paragraph (p) tag
paragraph = soup.find("p")
if paragraph:
    print(f"Paragraph: {paragraph.text.strip()}")

# Extract and print the link within the anchor (a) tag
link = soup.find("a")
if link:
    print(f'Link: {link["href"]}')

# Extract and print the source (src) attribute of the image tag
image = soup.find("img")
if image:
    print(f'Image Source: {image["src"]}')

# Extract and print the list items within the unordered list (ul) tag
ul = soup.find("ul")
if ul:
    print("Unordered List:")
    for li in ul.find_all("li"):
        print(f"- {li.text}")

# Extract and print the list items within the ordered list (ol) tag with start attribute
ol = soup.find("ol")
if ol:
    start_value = int(ol.get("start", "1"))
    print("Ordered List:")
    for li in ol.find_all("li"):
        print(f"{start_value}. {li.text}")
        start_value += 1
