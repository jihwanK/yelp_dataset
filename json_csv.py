import json
import csv

biz_json_file = open('business.json', 'r', encoding='utf-8')
rev_json_file = open('review.json', 'r', encoding='utf-8')
tip_json_file = open('tip.json', 'r', encoding='utf-8')

biz_csv_file = open('business.csv', 'r', encoding='utf-8', newline='')
rev_csv_file = open('review.csv', 'r', encoding='utf-8', newline='')
tip_csv_file = open('tip.csv', 'r', encoding='utf-8', newline='')

