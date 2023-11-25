import os
from bs4 import BeautifulSoup


def read_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def scrape_products(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    products = []

    product_listings = soup.find_all("div", class_="product-tuple-listing")
    for listing in product_listings:
        title = listing.find("div", class_="product-title").text.strip()
        price = listing.find("div", class_="product-price").text.strip()
        rating_count = listing.find("div", class_="product-rating-count").text.strip()

        products.append({"title": title, "price": price, "rating_count": rating_count})

    return products


file_path = "./EXAM/Q1.html"
base_url = "file://" + os.path.abspath(file_path)

num_pages = 3

for page in range(1, num_pages + 1):
    url = f"{base_url}/page{page}" if page > 1 else base_url
    html_content = read_html_file(file_path)

    if html_content:
        products = scrape_products(html_content)

        for product in products:
            print(
                f"Title: {product['title']}, Price: {product['price']}, Rating Count: {product['rating_count']}"
            )


"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")

input_field = driver.find_element_by_name("username")
input_field.send_keys("your_username")

button = driver.find_element_by_id("login_button")
button.click()

driver.quit()


"""
