import mysql.connector, pickle, sys

if len(sys.argv) != 1:
    print ("Enter passwrd of db as argument")
    sys.exit()
pwd = sys.argv[0]

cnx = mysql.connector.connect(user='root', password=pwd, host='54.65.177.207', database='toonbox')
cursor = cnx.cursor()

add_webtoon = ("INSERT INTO webtoon "
        "(author, genre, finished, title, picture, rating, last_update, introduction) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

f = open('naver.dump', 'rb')
toons = pickle.load(f);
f.close()

for toon in toons:
    data_webtoon = (toon['author'], toon['genre'], toon['finished'], toon['title'], toon['picture'], toon['rating'], str(toon['last_update']), toon['introduction'])
    cursor.execute(add_webtoon, data_webtoon)
cnx.close()
