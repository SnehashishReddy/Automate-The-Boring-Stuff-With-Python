import bs4, requests
from twilio.rest import Client

accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+12063374251'
myPhoneNumber = '+919182364810'

def scraper():
    site = 'https://weather.com/weather/today/l/d7f5a4af529e40b0a82d339e5467e89458e5ad5e2cf0ffdd05c853ed3e98fd38'
    request = requests.get(site)
    soup = bs4.BeautifulSoup(request.text, 'html.parser')
    currentWeather = ((soup.select('#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div.CurrentConditions--precipValue--RBVJT > span'))[0].getText()).lower()
    currentPercentage = int(currentWeather[:1])
    
    if currentPercentage > 35:
        return True
    else:
        return False

if scraper == True:
    rainMessage = twilioCli.messages.create(body = 'Hey bro! Don\'t forget to take an umbrella while going out today', from_ = myTwilioNumber, to = myPhoneNumber)

# This program should be run daily using Crontab
