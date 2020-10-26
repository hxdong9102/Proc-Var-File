# ---------------------------------------------------------------------
# Title: extract_web_lbl.py
# Description: extract labels from web, then write labels to file.
# Dependency: the prerequisites is webinfo_param.csv exist.
# Author: Dong Haixia
# Date: 2020-10-26
# ---------------------------------------------------------------------

# import libraries
import requests
from lxml import etree
import csv

# transform requests to requests session
xqySession = requests.session()

# acquire login token
url = "http://boweifeng.xueqingyun.com/user/sign-in/login"
responses = xqySession.get(url).text
# transform the response to DOM format
doc = etree.HTML(responses)
# get token value
token=doc.xpath('//meta[@name="csrf-token"]/@content')[0]

# required userinfo for the login process
userinfo={"_csrf":token,
          "LoginForm[identity]":"xzmadmin",
          "LoginForm[password]":"51testing",
          "LoginForm[rememberMe]":"0",
          "login-button":""}
result = xqySession.post(url, userinfo).text


# extract lables function
def extract_lbl(testURL, testLBL, lbls_csv):

    testRes = xqySession.get(testURL).text
    # format the testRes to DOM
    testDoc = etree.HTML(testRes)
    # extract labels from the testing web
    lbls = testDoc.xpath('//form//'+testLBL+'/text()')

    # write lbls to lbls_csv file
    with open (lbls_csv+".csv", 'w', newline="", encoding='utf-8-sig') as lblsfile:
        lblswrite = csv.writer(lblsfile)
        lblswrite.writerow(lbls)


# write lbls to csv (row[0].csv) file
webinfo_param = "webinfo_param.csv"

with open (webinfo_param, 'r') as webinfo:
    rows = csv.reader(webinfo)
    for row in rows:
        # print(row[0], row[1], row[2])
        extract_lbl(row[1], row[2], row[0])
