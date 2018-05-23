import requests
import pprint
import sys
import random
import json
r = json.load(open("C:\\Users\\p.mykhailyk\\Seafile\\p4ne_training\\card3.json"))
#print(r)
list1=[]
for part in r:  #numbers population
 #   list = list + [random.randint(10000000, 99999999)]
#    string = part(['CreditCard']['CardNumber'])
  #  print(part['CreditCard']['CardNumber'])
    st = part['CreditCard']['CardNumber']
    list1 = list1 + [str(st)]
for i in range(0, len(list1)):
    string = 'https://lookup.binlist.net/' + list1[i]
    r = requests.get(string)
    if 200<=r.status_code<=299:
 #       print(r.json())
        mass = r.json()
        if mass['bank'] != {}:
            print(mass['bank']['name'])
#print(list1)


#string='https://lookup.binlist.net/'+ li[5]
#r = requests.get(string)
#print(r)
#print(r.status_code)
#print(list)
#mass=(r.json())
#print(mass)
#print(mass["bank"]["name"])


