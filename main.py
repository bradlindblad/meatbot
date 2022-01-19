
from bs4 import BeautifulSoup as bs
import requests
import telepot

chat_id = 509047904
api_key = "5090479049:AAFKlZFwLsIkttkgMvTgtU0OGTFEwChXPD4"

def getSpecials(msg):
    URL = "http://www.meatsbyjohnandwayne.com/weeklyspecials.html"

    response = requests.get(URL)

    html = response.content
    soup = bs(html, "lxml")

    answer = soup.find("td").\
        text.\
        replace('\n', '').\
        replace('\xa0', '').\
        replace('(function(d, s, id) {\r  var js, fjs = d.getElementsByTagName(s)[0];\r  if (d.getElementById(id)) return;\r  js = d.createElement(s); js.id = id;\r  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.5";\r  fjs.parentNode.insertBefore(js, fjs);\r}(document, \'script\', \'facebook-jssdk\'));', '')

    return answer

def send_telegram_message():
    
    bot = telepot.Bot(api_key)
    bot.getMe()
    bot.sendMessage(1690960383, msg)


if __name__ == "__main__":
    
    # Get the specials
    meats = getSpecials()
    
    send_telegram_message(meats)
    
    
