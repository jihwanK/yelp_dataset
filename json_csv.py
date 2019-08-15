import json
import csv


biz_json_file = open('../business.json', 'r', encoding='utf-8')
rev_json_file = open('../review.json', 'r', encoding='utf-8')
tip_json_file = open('../tip.json', 'r', encoding='utf-8')

biz_csv_file = open('../business.csv', 'w', encoding='utf-8', newline='')
rev_csv_file = open('../review.csv', 'w', encoding='utf-8', newline='')
tip_csv_file = open('../tip.csv', 'w', encoding='utf-8', newline='')



############
# business #
############
lines = biz_json_file.readlines()
writer = csv.writer(biz_csv_file)
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
  
  row = [bid, name, city, state, stars, rev_cnt, cat]

  writer.writerow(row)

biz_json_file.close()
biz_csv_file.close()
print('converting business is done')


##########
# review #
##########
lines = rev_json_file.readlines()
writer = csv.writer(rev_csv_file)
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
  
  row = [rid, uid, bid, stars, text]

  writer.writerow(row)

rev_json_file.close()
rev_csv_file.close()
print('converting review is done')


#######
# tip #
#######
lines = tip_json_file.readlines()
writer = csv.writer(tip_csv_file)
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

  row = [text, cmp_cnt, bid, uid]

  writer.writerow(row)

tip_json_file.close()
tip_csv_file.close()
print('converting tip is done')