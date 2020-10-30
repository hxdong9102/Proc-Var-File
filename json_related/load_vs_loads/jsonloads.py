# ------------------------------------------------------------
# --  Title: jsonload.py
# --  Description: read json encodded data from string.
# --  Author: Dong Haixia
# --  Date: 2020-10-28
# ------------------------------------------------------------

import json

developerJsonString = """{
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
"""

print("Start converting JSON string document to Python dictionary.")
developerDict = json.loads(developerJsonString)

print("Printing key and values:")
for key, value in developerDict.items():
    print(key, ":", value)

print("Done converting JSON string document to a dictionary.")