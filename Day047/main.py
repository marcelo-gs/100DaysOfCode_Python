from bs4 import BeautifulSoup
import requests
import smtplib

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36", 
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7"
}
product_url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
response = requests.get(product_url, headers=header)
response.raise_for_status()
amazon_response = response.text
#print(amazon_response)

BUY_PRICE = 100

soup = BeautifulSoup(amazon_response, "lxml")
price = soup.find(name="span", id="priceblock_ourprice")
price_as_float = float(price.getText().replace("$",""))
title = soup.find(id="productTitle").get_text().strip()

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP("smtp.google.com", port=587) as connection:
        connection.starttls()
        result = connection.login("email@email", "password.password")
        connection.sendmail(
            from_addr="email@email",
            to_addrs="email2@email",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
#◬