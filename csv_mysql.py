import mysql.connector
import csv

user = 'root'
password = 'qlalfqjsgh1!'
database = 'yelp'

conn = mysql.connector.connect(user=user, passwd=password, database=database)
cur = conn.cursor()

biz = open("../business.csv", "r", encoding="utf-8")
rev = open("../review.csv", "r", encoding="utf-8")
tip = open("../tip.csv", "r", encoding="utf-8")


lines = csv.reader(biz, delimiter=',')
for line in lines:
  sql = 'INSERT INTO business VALUES ( "{bid}", "{name}", "{city}", "{state}", "{stars}", "{review_count}", "{categories}" )'.format(bid=line[0], name=line[1], city=line[2], state=line[3], stars=line[4], review_count=line[5], categories=line[6])
  print(line)
  if len(line) != 7:
    print(len(line))
  #cur.execute(sql)
print('business done')

lines = csv.reader(rev, delimiter=',')
for line in lines:
  sql = 'INSERT INTO review VALUES ( "{rid}", "{uid}", "{bid}", "{star}", "{text}" )'.format(rid=line[0], uid=line[1], bid=line[2], star=line[3], text=line[4])
  print(line)
  if len(line) != 5:
    print(line)
  #cur.execute(sql)
print('review done')

lines = csv.reader(tip, delimiter=',')
for line in lines:
  sql = 'INSERT INTO tip VALUES ( "{text}", "{compliment_count}", "{bid}", "{uid}" )'.format(text=line[0], compliment_count=line[1], bid=line[2], uid=line[3])
  print(line)
  if len(line) != 4:
    print(line)
  #cur.execute(sql)
print('tip done')


conn.commit()
conn.close()
