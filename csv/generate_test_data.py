# ---------------------------------------------------------------------
# - Title: generate_test_data.py
# - Description: generate test data, and save the data to csv file.
# - Author: Dong Haxia
# - Date: 2020-9-13
# ---------------------------------------------------------------------

import csv
import datetime
from faker import Faker

# Create and open a csv file.
file = open("testdata.csv", "w", newline="")
# get the file object.
fwrite = csv.writer(file)
name = 'login'
faker = Faker(locale='zh_CN')
start = datetime.date.today()

for i in range(0, 100):
    num = str(i).zfill(5)
    loginName = name+num
    #print(loginName)
    userName = faker.name()
    # generate password.
    passwd = faker.password()
    #print(passwd)
    # generate idCard.
    idCard = faker.ssn(min_age=18, max_age=90)
    # generate a No with lengths=6.
    tNo = faker.random_number(digits=6)
    #print(tNo)
    # generate telephone number
    tel = faker.phone_number()
    # generate e-mail
    mail = faker.free_email()
    # generate end date.
    end = faker.date_between(start_date=start, end_date="+20d")
    # write date to csv file.
    fwrite.writerow([loginName, userName, passwd, idCard, tNo, tel, mail, start, end])

# close the generated file.
file.close()