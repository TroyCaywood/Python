import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
import os


EMAIL = os.getenv(EMAIL)
EMAIL_PW= os.getenv(EMAIL_PW)
PURCHASE_PRICE = 170


# Product URL and headers for request
URL = "https://www.amazon.com/NVIDIA-Shield-Android-Streaming-Performance/dp/B07YP9FBMM/ref=sr_1_2"
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/109.0.0.0 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'keep-alive',
            })


# Get product page text and create soup using LXML parser
response = requests.get(URL, headers=HEADERS)
product_page = response.text
soup = BeautifulSoup(product_page, "lxml")


# Get product price and product name. Strip extra returns and replace extraneous text with blank string.
price_tag = soup.find(name="span", class_="a-offscreen")
product_name = soup.find(id="productTitle").get_text().strip().replace("Streaming Media Player;"
                                                                       " 4K HDR movies, live sports,"
                                                                       " Dolby Vision-Atmos, AI-enhanced upscaling,"
                                                                       " GeForce NOW cloud gaming, Google Assistant"
                                                                       " Built-In, Works with Alexa", "")

# Get pricetag text, remove $ and convert to a float
price = float(price_tag.get_text().replace("$", ""))


# If price is less than or equal to the PURCHASE_PRICE variable, send an email
if price <= PURCHASE_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PW)

        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="some_email_address@gmail.com",
            msg=f"Subject: {product_name} is now {price}!\n\n{product_name} is now {price}! Hurry up and buy it!"
                f"\n\n{URL}"
        )
