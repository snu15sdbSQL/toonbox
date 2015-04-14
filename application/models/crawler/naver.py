import urllib, os
from bs4 import BeautifulSoup

base_url = "http://comic.naver.com/webtoon/genre.nhn?genre="
genres = ['episode', 'omnibus', 'story', 'daily', 'comic', 'fantasy', 
'action', 'drama', 'pure', 'sensibility', 'thrill', 'historical',
'sports']

cnt = 0		#index for matching a webtoon and its thumbnail
toons = []	#list of each dict describing a webtoon

for genre in genres:
	genre_url = base_url + genre
	html = urllib.urlopen(genre_url)
	soup = BeautifulSoup(html, "lxml")
	toon_list = soup.find_all("ul", "img_list")[0]

	for item in toon_list.find_all('li'):
		cnt += 1

		#retrieve a webtoon's info
		toon = {}
		toon['id'] = cnt
		toon['title'] = item.div.a['title']
		toon['author'] = item.dl.dd.a.text
		toon['rating'] = \
			item.find_all('div', 'rating_type')[0].strong.text
		toons.append(toon)

		#download thumbnail
		if not os.path.exists('./naver'):
			os.makedirs('./naver')
		img_url = item.div.a.img['src']
		img_filename = "./naver/" + str(cnt) + ".jpg"
		urllib.urlretrieve(img_url, img_filename)

		print "id: " + str(cnt) + "\ttitle:" + toon['title'] + "\tauthor:" + toon['author'] + "\trating:" + toon['rating']
