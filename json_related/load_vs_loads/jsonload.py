# ------------------------------------------------------------
# --  Title: jsonload.py
# --  Description: read json encodded data from a file.
# --  Author: Dong Haixia
# --  Date: 2020-10-28
# ------------------------------------------------------------

import json


print("Start to read json file")
# Open the JSON file
with open("jsonfile.json", "r") as readfile:
    result = json.load(readfile)


print("Decoded JSON DATA from file are:")
for key, value in result.items():
    print(key, ":", value)
print("Reading JSON file completed!")