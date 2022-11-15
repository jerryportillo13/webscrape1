
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font




#rank, release gross, dist

#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
page = urlopen(webpage)			
soup = BeautifulSoup(page, 'html.parser')

title = soup.title
print('**************')
print(title.text)
print('**************')
print()
#tables = soup.findAll('table')
#movie_table = tables[0] dont this because theres only one table 

movie_tablerows = soup.findAll('tr')


for x in range(1,6):
    
    td = movie_tablerows[x].findAll('td') #index 'x' skips the first row since it doesnt have 'td' tags 
    rank = td[0].text
    release = td[1].text
    total_gross = td[7].text
    dist = td[9].text
    theater = td[6].text

    

    print(rank)
    print(release)
    print(total_gross)
    print(dist)
    input()



