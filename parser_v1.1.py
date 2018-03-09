## for baitoru
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def findNode(soups):
	soupDiv = soups.find_all('article', class_='list-jobListDetail')

	for article in soupDiv:
		div = article.find('div', class_='pt02b')
		p = div.find('p').text
		pLink.append(p)

soupURL = 'https://www.baitoru.com/kyushu/jlist/page'
pLink = list()

for nums in range(500,1000):
    try:
    	soupPage = urlopen(soupURL + str(nums))
    	soup = BeautifulSoup(soupPage, 'html.parser')
    	findNode(soup)
    	print('page{}'.format(str(nums)))
    except urllib.error.HTTPError:
    	continue

f = open("company_bai222.csv", "w")
w = csv.writer(f, delimiter = ",")
w.writerows([x.split(',') for x in pLink])
print('Done..')
f.close()

'''
http://www.baitoru.com/tohoku/jlist/
http://www.baitoru.com/koshinetsu/jlist/
http://www.baitoru.com/kanto/jlist/
http://www.baitoru.com/tokai/jlist/
http://www.baitoru.com/kansai/jlist/
http://www.baitoru.com/chushikoku/jlist/
http://www.baitoru.com/kyushu/jlist/
'''
