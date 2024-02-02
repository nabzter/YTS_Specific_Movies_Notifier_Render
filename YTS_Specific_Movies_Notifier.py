import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook
import time
import pytz
from datetime import datetime

url = "https://yts.mx/"
webhook_url = "webhook_url"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

current_date = datetime.now().strftime("%d-%m-%Y")

def read_title_names():
    with open("movies_titles.txt", "r") as file:
        return {line.strip() for line in file}

def scrape_latest_titles():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    return [{"title": movie.text.strip(), "url": url + movie['href']} for movie in soup.select(".browse-movie-wrap a.browse-movie-title")[:4]]

def send_to_discord(title, url):
    DiscordWebhook(url=webhook_url, content=f"@everyone\n Latest movie: **{title}**\n Date: {current_date}\n URL: {url}").execute()
    print(f"Sent to Discord: {title}")

def remove_matching_title(title):
    with open("movies_titles.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.writelines(line for line in lines if line.strip() != title)
        file.truncate()

while True:
    latest_movies = scrape_latest_titles()
    stored_titles = read_title_names()

    print("Checking Movies...")

    for movie in latest_movies:
        title = movie["title"]
        url = movie["url"]
        if title in stored_titles:
            print(f"Match found: {title}")
            send_to_discord(title, url)
            remove_matching_title(title)
            print(f"Removed from the file: {title}")
        
    print("No Matching Movies Found")

    print("Waiting 15 Mins...")
    time.sleep(900)