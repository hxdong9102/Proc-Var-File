# ------------------------------------------------------------
# Title: weiboinfo_csv.py
# Description: write web info to a csv file.
# Author: Dong Haixia
# Date: 2020-10-26
# ------------------------------------------------------------

# import csv library
import csv

# web info that is needed written to a csv file
webinfo = [['stu', 'http://boweifeng.xueqingyun.com/schadmin/user/add-stu', 'label'],
['thr', "http://boweifeng.xueqingyun.com/schadmin/user/add-thr", 'label'],
['pro', "http://boweifeng.xueqingyun.com/schadmin/subject/create", 'th']]

# write info into the csvfile.
webinfo_param = "webinfo_param.csv"
with open(webinfo_param, 'w', newline='') as file:
    for i in webinfo:
        fwrite = csv.writer(file)
        fwrite.writerow(i)