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

    answer = (
        soup.find("td")
        .text.replace("\n", "")
        .replace("\xa0", "")
        .replace(
            "(function(d, s, id) {\r  var js, fjs = d.getElementsByTagName(s)[0];\r  if (d.getElementById(id)) return;\r  js = d.createElement(s); js.id = id;\r  js.src = \"//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.5\";\r  fjs.parentNode.insertBefore(js, fjs);\r}(document, 'script', 'facebook-jssdk'));",
            "",
        )
    )

    return answer


def send_telegram_message(msg):

    bot = telepot.Bot(API_KEY)
    bot.getMe()
    bot.sendMessage(MY_ID, msg)


if __name__ == "__main__":

    # Get the specials
    meats = getSpecials()

    send_telegram_message(meats)
