
from bs4 import BeautifulSoup as bs
import json
import requests
import telegram_send

chat_id = "5090479049"
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


# def send_telegram_message(message: str,
#                           chat_id: str,
#                           api_key: str,
#                           proxy_username: str = None,
#                           proxy_password: str = None,
# 		  proxy_url: str = None):
#     responses = {}

#     proxies = None
#     if proxy_url is not None:
#         proxies = {
#             'https': f'http://{username}:{password}@{proxy_url}',
#             'http': f'http://{username}:{password}@{proxy_url}'
#         }
#         headers = {'Content-Type': 'application/json',
#                    'Proxy-Authorization': 'Basic base64'}
#         data_dict = {'chat_id': chat_id,
#                      'text': message,
#                      'parse_mode': 'HTML',
#                      'disable_notification': True}
#         data = json.dumps(data_dict)
#         url = f'https://api.telegram.org/bot{api_key}/sendMessage'
#         response = requests.post(url,
#                                  data=data,
#                                  headers=headers,
#                                  proxies=proxies,
#                                  verify=False)
#         return response

if __name__ == "__main__":
    
    # Get the specials
    meats = getSpecials()
    
    telegram_send.send(messages=[meats])