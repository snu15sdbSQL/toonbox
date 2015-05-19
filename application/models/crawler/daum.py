import urllib2, urllib, os, pickle, time
from bs4 import BeautifulSoup

maxbuf = 10485760

### load html
# from pyvirtualdisplay import Display

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # use virtual display to launch Firefox within CLI
# display = Display(visible=0, size=(800, 600))
# display.start()

# driver = webdriver.Firefox()
# driver.implicitly_wait(10)
# driver.get("http://m.webtoon.daum.net/m/#page_no=26&type=scoreList")
# try: #wait until list is fully loaded
# 	element = WebDriverWait(driver, 20).until(
# 		EC.presence_of_element_located((By.CSS_SELECTOR, ".list_comm > ul > li"))
# 	)
# finally:
# 	html = driver.page_source

# driver.quit()
# display.stop()

# with open('daum_html.dump', 'wb') as f:
# 	pickle.dump(html, f)

with open('daum_html.dump', 'rb') as f:
	html = pickle.load(f)

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
	toon = {}

	toon_title = item.find_all('strong', 'tit')[0]
	#remove text indicating 'for adult'
	span19 = toon_title.find('span', 'ico_comm')
	if span19 != None:
		span19.replace_with('')
	toon['title'] = toon_title.text
	toon['author'] = toon_author.text
	toon['rating'] = item.find('strong', 'point').text
	last_update = item.select('.time')[0].text
	if len(last_update) > 10:
		toon['last_update'] = last_update[:10].replace('.','-')
		toon['finished'] = int(int((toon['last_update'])[0:4]) < 2015)
	else:
		toon['last_update'] = time.strftime("%Y-%m-%d")
		toon['finished'] = 0
	
	#get each webtoon's page for detail
	toon['url'] = "http://m.webtoon.daum.net/" + item.find('a', 'cont')['href'];
	toon['site'] = "daum"
	res = urllib2.urlopen(toon['url'])
	toon_html = res.read(maxbuf)
	res.close
	
	toon_soup = BeautifulSoup(toon_html, "lxml")
	intro= toon_soup.findAll(attrs={"property":"og:description"})
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
	toon['picture'] = str(cnt) + ".jpg"

	print "finish:" + str(toon['finished']) + " id: " + str(cnt) + "\ttitle:" + toon['title'] + "\tauthor:" + toon['author'] + "\trating:" + toon['rating'] + "\tlast_update:" + toon['last_update'] + "\tintro:" + toon['introduction']

#save crawling result
with open('daum.dump', 'wb') as f:
	pickle.dump(toons, f)