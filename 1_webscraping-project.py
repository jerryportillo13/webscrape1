from itertools import count
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import tw_Twiliokeys2
from twilio.rest import Client

url = 'https://www.investing.com/crypto/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title
print('******************************************')
print(title.text)
print('******************************************')
print()

tablerows = soup.findAll('tr')
#print(tablerows)

#Getting top 5 cryptos 
for x in range(1,6):
    td = tablerows[x].findAll('td')
    rank_num = td[0].text
    name = td[2].text
    tickerSym = td[3].text
    current_price = round(float(td[4].text.replace(",", "")),2)
    perct_change = td[8].text
    
    #corresponding/initial price calc 
    intial_calc_perct = float(td[8].text.replace("%", ""))
    perctToDecimal = float(intial_calc_perct/100)
    intial_price = round(float(current_price - (current_price*perctToDecimal)),2)

    print("***************")
    print(f"Rank: {rank_num}")
    print(f"Crypto Name:{name}")
    print(f"Crypto Ticker Symbol:{tickerSym}")
    print(f"Initial/Corresponding Price (24 hours): ${intial_price}")
    print(f"Current Price: ${current_price}")
    print(f"Percent change (24 hours): {perct_change}")
    print("***************")
    input()


#alert
client = Client(tw_Twiliokeys2.accountSID, tw_Twiliokeys2.authToken)
TwilioNumber = "+12545227229" #twilio number bought
myCell = "+12107447975" #my personal phone number 

current_price_alert = float(td[4].text.replace(",", ""))
textmsg = client.messages.create(to=myCell, from_=TwilioNumber, body= "Bitcoin is below $40,000")
textmsg1 = client.messages.create(to=myCell, from_=TwilioNumber, body= "Ethereum is below $3,000")

#alert for BTC
if name == 'Bitcoin' and current_price_alert >= 400000:
    print('No text sent')
else:
    print(textmsg.status)
    print('Text Sent')
    

#alert for ETH
if name == 'Ethereum' and current_price_alert >= 3000:
    print('No text sent')   
else:
    print(textmsg1.status)
    print('Text Sent')



