import urllib, os

from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

# use virtual display to launch Firefox within CLI
display = Display(visible=0, size=(800, 600))
display.start()

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://m.webtoon.daum.net/m/#page_no=26&type=scoreList")
try: #wait until list is fully loaded
	element = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, ".list_comm > ul > li"))
	)
finally:
	html = driver.page_source

driver.quit()
display.stop()

soup = BeautifulSoup(html, "lxml")
thumbs = soup.select('.list_comm > ul')[0]

cnt = 0
toons = []	#list of each webtoons' dict

for item in thumbs.find_all('li'):
	#in case of temporary unpublishing
	toon_author = item.find('span', 'txt_name')
	if toon_author == None:
		continue

	cnt += 1
	#dict for each webtoon's information
	toon = {}

	toon_title = item.find_all('strong', 'tit')[0]
	#remove text indicating 'for adult'
	span19 = toon_title.find('span', 'ico_comm')
	if span19 != None:
		span19.replace_with('')
	toon['title'] = toon_title.text

	toon['author'] = toon_author.text
	toon['rating'] = item.find('strong', 'point').text
	toon['last_update'] = item.select('.time')[0].text[:10].replace('.','-')

	#get each webtoon's page for detail
	toon_url = "http://m.webtoon.daum.net/" + item.find('a', 'cont')['href'];
	toon_html = urllib.urlopen(toon_url)
	toon_soup = BeautifulSoup(toon_html, "lxml")

	intro= soup.findAll(attrs={"property":"og:description"})
	if len(intro) != 0:
		toon['introduction'] = intro[0]['content'].rsplit('l',1)[0]
	else:
		toon['introduction'] = "ADULT TOON REQUIRES LOGIN. UPDATE IT MANUALLY"

	toons.append(toon)

	#download thumbnail
	if not os.path.exists('./daum'):
		os.makedirs('./daum')
	img_url = item.find('img', '')['data-src']
	img_filename = "./daum/" + str(cnt) + ".jpg"
	urllib.urlretrieve(img_url, img_filename)

	print "id: " + str(cnt) + "\ttitle:" + toon['title'] + "\tauthor:" + toon['author'] + "\trating:" + toon['rating'] + "\tlast_update:" + toon['last_update'] + "\tintro:" + toon['introduction']
