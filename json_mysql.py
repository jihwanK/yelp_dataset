import json
import csv
import mysql.connector


user = 'root'
password = 'qlalfqjsgh1!'
database = 'yelp'

conn = mysql.connector.connect(user=user, passwd=password, database=database)
cur = conn.cursor()


miss_biz_num = 0
miss_rev_num = 0
miss_tip_num = 0


biz_json_file = open('../business.json', 'r', encoding='utf-8')
rev_json_file = open('../review.json', 'r', encoding='utf-8')
tip_json_file = open('../tip.json', 'r', encoding='utf-8')


############
# business #
############
lines = biz_json_file.readlines()
for line in lines:
  line_dict = json.loads(line)

  try:
    bid = line_dict['business_id'].replace('"', '\\"').replace("'", "\\'")
  except:
    bid = line_dict['business_id']
  
  try:
    name = line_dict['name'].replace('"', '\\"').replace("'", "\\'")
  except:
    name = line_dict['name']

  try:
    city = line_dict['city'].replace('"', '\\"').replace("'", "\\'")
  except:
    city = line_dict['city']
  
  try:
    state = line_dict['state'].replace('"', '\\"').replace("'", "\\'")
  except:
    state = line_dict['state']  

  stars = line_dict['stars']
  
  rev_cnt = line_dict['review_count']
  
  try:
    cat = line_dict['categories'].replace('"', '\\"').replace("'", "\\'")
  except:
    cat = line_dict['categories']
  
  sql = 'INSERT INTO business VALUES ( "{bid}", "{name}", "{city}", "{state}", "{stars}", "{review_count}", "{categories}" )'.format(bid=bid, name=name, city=city, state=state, stars=stars, review_count=rev_cnt, categories=cat)
  try:
    cur.execute(sql)
  except:
    miss_biz_num += 1
    print("(" + str(miss_biz_num) + "): " + bid + ' made problem')
  #print(name)

biz_json_file.close()
print('converting business is done')
conn.commit()


##########
# review #
##########
lines = rev_json_file.readlines()
for line in lines:
  line_dict = json.loads(line)

  try:
    rid = line_dict['review_id'].replace('"', '\\"').replace("'", "\\'")
  except:
    rid = line_dict['review_id']

  try:
    uid = line_dict['user_id'].replace('"', '\\"').replace("'", "\\'")
  except:
    uid = line_dict['user_id']  

  try:
    bid = line_dict['business_id'].replace('"', '\\"').replace("'", "\\'")
  except:
    bid = line_dict['business_id']
  
  stars = line_dict['stars']

  try:
    text = line_dict['text'].replace('"', '\\"').replace("'", "\\'")
  except:
    text = line_dict['text']
  
  sql = 'INSERT INTO review VALUES ( "{rid}", "{uid}", "{bid}", "{stars}", "{text}" )'.format(rid=rid, uid=uid, bid=bid, stars=stars, text=text)
  try:
    cur.execute(sql)
  except:
    miss_rev_num += 1
    print("(" + str(miss_rev_num) + "): " + bid + ' made problem')
 # print(bid)

rev_json_file.close()
print('converting review is done')
conn.commit()


#######
# tip #
#######
lines = tip_json_file.readlines()
for line in lines:
  line_dict = json.loads(line)

  try:
    text = line_dict['text'].replace('"', '\\"').replace("'", "\\'")
  except:
    text = line_dict['text']
  
  cmp_cnt = line_dict['compliment_count']

  try:
    bid = line_dict['business_id'].replace('"', '\\"').replace("'", "\\'")
  except:
    bid = line_dict['business_id']
  
  try:
    uid = line_dict['user_id'].replace('"', '\\"').replace("'", "\\'")
  except:
    uid = line_dict['user_id']  

  sql = 'INSERT INTO tip VALUES ( "{text}", "{compliment_count}", "{bid}", "{uid}" )'.format(text=text, compliment_count=cmp_cnt, bid=bid, uid=uid)
  try:
    cur.execute(sql)
  except:
    miss_tip_num += 1
    print("(" + str(miss_tip_num) + "): " + bid + ' made problem')
  #print(bid)

tip_json_file.close()
print('converting tip is done')
conn.commit()

conn.close()
