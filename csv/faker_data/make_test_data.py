# ------------------------------------------------------------
# Title: make_test_data.py
# Description: make test data to a csv file with head v2.0
# Author: Dong Haixia
# Date: 2020-10-22
# ------------------------------------------------------------

# import libraries
import csv
from faker import Faker


f = Faker(locale='zh_CN')

csvfile = "person.csv"

with open(csvfile, "a+", newline="", encoding='utf-8-sig') as file:
    for i in range(0, 100):
        name = f.name()
        company = f.company()
        job = f.job()
        mail = f.email()
        addr = f.address()
        tel = f.phone_number()
        birth = f.date(pattern='%Y-%m-%d')

        # append data to the target csv file
        fwrite = csv.writer(file)
        fwrite.writerow([name, company, job, mail, addr, tel, birth])