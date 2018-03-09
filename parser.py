from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

# soupURL = 'https://www.baitoru.com/kanto//jlist/'
# for nums in range(2,5):
#     soupPage = urlopen(soupURL + str(nums))
#     soup = BeautifulSoup(soupPage, 'html.parser')
#     soupDiv = soup.find_all('article', class_='list-jobListDetail')

#     pLink = list()

#     for article in soupDiv:
#         div = article.find('div', class_='pt02b')
#         p = div.find('p').text
#         pLink.append(p)

#     f = open("company_bai2.csv", "w")
#     w = csv.writer(f, delimiter = ",")
#     w.writerows([x.split(',') for x in pLink])
#     f.close()

soupURL = 'https://www.baitoru.com/kanto/jlist/'
soupPage = urlopen(soupURL)
soup = BeautifulSoup(soupPage, 'html.parser')
soupDiv = soup.find_all('article', class_='list-jobListDetail')

pLink = []

for article in soupDiv:
    div = article.find('div', class_='pt02b')
    p = div.find('p').text
    pLink.append(p)
    # print(p)

f = open("company_bai2.csv", "w")
w = csv.writer(f, delimiter = ",")
w.writerows([x.split(',') for x in pLink])
f.close()
