import requests
from bs4 import BeautifulSoup
import pandas as pd

try:
    # Website URL
    url = "https://quotes.toscrape.com/"

    # Send request
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Lists to store data
    quotes_list = []
    authors_list = []

    # Find all quote blocks
    quotes = soup.find_all("div", class_="quote")

    # Extract data
    for quote in quotes:
        text = quote.find("span", class_="text").get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)

        quotes_list.append(text)
        authors_list.append(author)

    # Create DataFrame
    df = pd.DataFrame({
        "Quote": quotes_list,
        "Author": authors_list
    })

    # Save CSV with UTF-8 encoding
    df.to_csv("quotes_dataset.csv", index=False, encoding="utf-8-sig")

    print("Dataset created successfully!")
    print("Total Quotes:", len(df))
    print("\nFirst 5 Records:")
    print(df.head())

except Exception as e:
    print("Error occurred:")
    print(e)