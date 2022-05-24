import json

from uuid import uuid4
trialdata=[{



"name": "toyota",
"phonenumber": 7112233,
"address": "2345",



"name": "Kia",
"phonenumber": 7112233,
"address": "2345",


"name": "ali",
"phonenumber": 1122,
"address": "2345",


"name": "corny",
"phonenumber": 1144,
"address": "2345",

}]

for user in trialdata:
     user_id = str(uuid4())
     with open('trialdata.json', 'w') as f:
        json.dump(trialdata, f, indent=2)



   

