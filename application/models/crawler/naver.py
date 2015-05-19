import urllib, os, sys, pickle
from bs4 import BeautifulSoup

if len(sys.argv) != 1:
    print ("Enter thumbnail folder as argument(ending with '/')")
    sys.exit()
path = sys.argv[0]

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

		#get each webtoon's page for detail
		toon_url = 'http://comic.naver.com' + item.div.a['href']
		toon_html = urllib.urlopen(toon_url)
		toon_soup = BeautifulSoup(toon_html, "lxml")
		detail = toon_soup.select('.comicinfo > .detail')[0]

		toon = {}
		toon['author'] = detail.find("span", "wrt_nm").text
		toon['finished'] = int(item.select('.finish') == [])
		toon['title'] = item.div.a['title']
		toon['rating'] = item.find_all('div', 'rating_type')[0].strong.text
		toon['last_update'] = item.select('.date2')[0].text.replace('.','-')
		toon['introduction'] = detail.find('p').text.replace('\n', '')
		toon['url'] = toon_url
		toon['site'] = "naver"
		toons.append(toon)

		#download thumbnail
		if not os.path.exists('./naver/'):
			os.makedirs('./naver/')
		img_url = toon_soup.select('.thumb img')[0]['src']
		img_filename = './naver/' + str(cnt) + ".jpg"
		urllib.urlretrieve(img_url, img_filename)
		toon['picture'] = str(cnt) + ".jpg"

		#progress bar
		sys.stdout.write("\r" + str(cnt) + " " + '#'*(cnt%10) + ' '*(10-cnt%10)
			+ toon['title'][:30] + ' '*(30-len(toon['title'])))
		sys.stdout.flush()

		# print "\ttitle:" + toon['title'] + "\tauthor:" + toon['author'] + "\trating:" + toon['rating'] + "\tintroduction:" + toon['introduction']

#save crawling result
with open('naver.dump', 'wb') as f:
	pickle.dump(toons, f)