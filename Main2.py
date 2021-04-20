import json
from Function import *

gdata = open('output.json')

data = json.load(gdata)


count = 0
for i in data:
    if overweight(i['BMI_CATEGORY']) == 'True':
    	count = count + 1

print(count)
