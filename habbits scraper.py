import requests
from bs4 import BeautifulSoup

url = "https://camillestyles.com/wellness/morning-routine/healthy-daily-habits/"

def scrape():
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')

    habits = [habit.text.strip() for habit in soup.find_all("h3", class_="wp-block-heading")] #the habits have a bunch of extra text i dont need so i am removing it using class_="wp-block-heading"
    return habits[:5]

print(scrape())
