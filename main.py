from bs4 import BeautifulSoup as bs
from decouple import config
import requests
import sys
import telepot


MY_ID = config("MY_ID")
API_KEY = config("API_KEY")

def getSpecials():
    URL = "http://www.meatsbyjohnandwayne.com/weeklyspecials.html"

    response = requests.get(URL)

    html = response.content
    soup = bs(html, "lxml")

    specials = soup.select('.specials-wrap div')
    clean_specials = [i.text for i in specials]
    cleaner_specials = [i.replace("  ", '') for i in clean_specials]
    cleanest_specials = [i.replace("\n", ' ').strip() for i in cleaner_specials]

    
    return cleanest_specials


def send_telegram_message(msg):

    bot = telepot.Bot(API_KEY)
    bot.getMe()
    bot.sendMessage(MY_ID, msg)


if __name__ == "__main__":

    # Get the specials
    meats = getSpecials()

    send_telegram_message(meats)
