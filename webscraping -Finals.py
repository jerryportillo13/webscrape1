from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

url = 'https://registrar.web.baylor.edu/exams-grading/fall-2022-final-exam-schedule'

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

#looking for table class  
tables = soup.findAll('table')

finals_table = tables[1]
#print(finals_table)

#table row
tr = finals_table.findAll('tr')
myclasses_file = open('classes.csv', 'r')
myclasses = csv.reader(myclasses_file, delimiter=',')

next(myclasses)
for rec in myclasses:
    day = rec[0]
    time = rec[1]

    for row in tr:
        td = row.findAll('td')
        if td:
            sch_day = td[0].text
            sch_time = td[1].text
            sch_exam_day = td[2].text
            sch_exam_time = td[3].text

            if sch_day == day and sch_time == time:
                print(f"Exam Day and Time: {sch_exam_day, sch_exam_time} for my class on: {day}, at {time}")
                #print(f"Exam time:{sch_exam_time} for class time: {time}")






