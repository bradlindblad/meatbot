
from bs4 import BeautifulSoup as bs
import requests
from telethon import TelegramClient

chat_id = 509047904
api_key = "5090479049:AAFKlZFwLsIkttkgMvTgtU0OGTFEwChXPD4"

def getSpecials():
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

# def send_telegram_message():
    
#     client = TelegramClient('session_name', chat_id, api_key)
#        #Start the process
#     client.start()
#        #Send the message
#     client.send_message(chat_id = chat_id, msg = "wahtupp")


if __name__ == "__main__":
    
    # Get the specials
    meats = getSpecials()
    
    # telegram_send.send(messages=[meats],conf = "getmeat.conf")
    # send_telegram_message(meats)
    print(meats)
    