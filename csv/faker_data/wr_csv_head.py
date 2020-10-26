# ------------------------------------------------------------
# Title: write_csv_head.py
# Description: write head for a empty csv file v1.0
# Author: Dong Haixia
# Date: 2020-10-22
# ------------------------------------------------------------

# import csv library
import csv


def extract_lbl(content, lbls_csv):    
    # write lbls to lbls_csv file
    with open (lbls_csv, 'w', newline="", encoding='utf-8-sig') as lblsfile:
        lblswrite = csv.writer(lblsfile)
        lblswrite.writerow(content)      


content = ['姓名', '单位', '职位', '邮箱', '地址', '电话号码', '出生日期']
file_path = "person.csv"

extract_lbl(content, file_path)