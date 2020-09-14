# -------------------------------------------------
# - Title: read_test_data.py
# - Description: read data from a csv file.
# - Author: Dong Haxia
# - Date: 2020-9-13
# -------------------------------------------------

import csv

# open the csv file
file = open("testdata.csv", "r")
rows = csv.reader(file)

for data in rows:
    #print(data)
    loginName = data[0]
    userName = data[1]
    passwd = data[2]
    idCard = data[3]
    tNo = data[4]
    tel = data[5]
    mail = data[6]
    startDate = data[7]
    endDate = data[8]

# close the csv file
file.close()