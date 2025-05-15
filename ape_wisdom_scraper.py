import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
from tabulate import tabulate
import os

# --- Constants ---
BASE_URL = "https://www.apewisdom.io/"
HEADERS = {"User-Agent": "Mozilla/5.0"}
OUTPUT_DIR = "./ape_wisdom_data/"
RETRY_ATTEMPTS = 3
RETRY_DELAY = 2  # seconds


def fetch_html(url, retries=RETRY_ATTEMPTS):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Attempt {attempt+1}/{retries} failed: {e}")
            time.sleep(RETRY_DELAY)
    raise Exception("Failed to fetch data after multiple attempts.")


def parse_ape_wisdom(html):
    soup = BeautifulSoup(html, "html.parser")
    
    # Ensure only the first table is selected
    table = soup.find("table")  # Select only the first table
    if not table:
        raise Exception("Table not found on Ape Wisdom.")

    headers = [th.text.strip() for th in table.find_all("th")]
    rows = []

    for tr in table.find_all("tr")[1:]:  # Skip header
        cols = [td.text.strip() for td in tr.find_all("td")]
        if len(cols) == len(headers):
            rows.append(cols)

    df = pd.DataFrame(rows, columns=headers)
    return clean_data(df)


def clean_data(df):
    def to_int(x):
        return int(x.replace(",", "").replace("▲", "").replace("▼", "").strip() or 0)

    # Remove unwanted columns if they exist
    columns_to_remove = ["Trend (30 days)", "Rank Change"]
    df = df.drop(columns=[col for col in columns_to_remove if col in df.columns], errors="ignore")

    # Drop the first column
    if not df.empty:
        df = df.iloc[:, 1:]  # Remove the first column by slicing

    if "Mentions" in df.columns:
        df["Mentions"] = df["Mentions"].apply(to_int)

    if "Upvotes" in df.columns:
        df["Upvotes"] = df["Upvotes"].apply(to_int)

    return df


def save_to_csv(df):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}ape_wisdom_{timestamp}.csv"
    df.to_csv(filename, index=False)
    print(f"[✔] Data saved to {filename}")


def display_top(df, sort_by="Mentions", top_n=15):
    if sort_by not in df.columns:
        print(f"[!] Column '{sort_by}' not found, skipping display.")
        return
    sorted_df = df.sort_values(by=sort_by, ascending=False).head(top_n)
    print(tabulate(sorted_df, headers="keys", tablefmt="fancy_grid", showindex=False))


def main():
    html = fetch_html(BASE_URL)
    df = parse_ape_wisdom(html)

    print("\n📈 Top 30 Trending Tickers (by Mentions):")
    display_top(df, sort_by="Mentions", top_n=30)  # Changed top_n to 30

    save_to_csv(df)


if __name__ == "__main__":
    main()
