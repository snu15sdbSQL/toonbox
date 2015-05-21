import mysql.connector, pickle, sys

if len(sys.argv) != 3:
	print len(sys.argv)
	print ("Enter passwrd of db and path as argument")
	sys.exit()
pwd = sys.argv[1]
dump = sys.argv[2]

cnx = mysql.connector.connect(user='root', password=pwd, host='54.65.177.207', database='toonbox')
cursor = cnx.cursor()

add_webtoon = ("INSERT INTO webtoon "
        "(author, site, finished, title, picture, rating, last_update, introduction, url) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

f = open(dump, 'rb')
toons = pickle.load(f);
f.close()

for toon in toons:
	data_webtoon = (toon['author'], toon['site'], toon['finished'], toon['title'], toon['picture'], toon['rating'], str(toon['last_update']), toon['introduction'], toon['url'])
	cursor.execute(add_webtoon, data_webtoon)
	cnx.commit()
cnx.close()
