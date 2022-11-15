# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from dataclasses import replace
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'

# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

table_rows = soup.findAll("tr")
'''
#50 states
for row in table_rows[2:52]:
    td = row.findAll("td")
    print(td[0].text)
    input()
'''
#state name, total death, total cases
#total tests, total population 


state_worst_death = ''
state_best_death = ''
high_death_ratio = 0.0
low_death_ratio = 100.00

state_worst_test = ''
state_best_test = ''
high_test_ratio = 0.0
low_test_ratio = 100.00



counter = 1
for row in table_rows[2:52]:
    td = row.findAll("td")
    state_name = td[1].text
    tot_cases = int(td[2].text.replace(",", ""))
    tot_death = int(td[4].text.replace(",", ""))
    tot_test = int(td[10].text.replace(",", ""))
    population = int(td[12].text.replace(",", ""))
    
    death_rate = round((tot_death/tot_cases) * 100,2)
    test_rate = round((tot_test/population) * 100,2)

    if death_rate > high_death_ratio:
        state_worst_death = state_name
        high_death_ratio = death_rate

    if death_rate < low_death_ratio:
        state_best_death = state_name
        low_death_ratio = death_rate

    if test_rate > high_test_ratio:
        state_best_test = state_name
        high_test_ratio = test_rate

    if test_rate < low_test_ratio:
        state_worst_test = state_name
        low_test_ratio = test_rate

    print(f"State with worst death rate:{state_worst_death}")
    print(f"Death Rate: {high_death_ratio}%")
    print()
    print()
    print(f"State with best death rate:{state_best_death}")
    print(f"Death Rate: {low_death_ratio}%")
    print()
    print()
    print(f"State with worst test rate:{state_worst_test}")
    print(f"Test Rate: {low_test_ratio}%")
    print()
    print()
    print(f"State with best test rate:{state_best_test}")
    print(f"Test Rate: {high_test_ratio}%")
    print()
    print()



    
    









#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

