#!/bin/bash

python3 dbsetup.py
python3 json_csv.py
csv_mysql.py