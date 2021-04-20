import json
from Function import *

gdata = open('data.json')

data = json.load(gdata)





with open("data.json") as f:
    json_ob = json.load(f)

entries = []
for i in json_ob:
	x = i['HeightCm']/100
	cal_bmi = calBMI(i['WeightKg'],x)
	bmi_category = bmicategory(cal_bmi)
	health_risk = healthrisk(cal_bmi)
	final = {"Gender":i['Gender'],"HeightCm":i['HeightCm'],"WeightKg":i['WeightKg'],"Bmi":cal_bmi,"BMI_CATEGORY":bmi_category,"Health_Risk":health_risk}
	entries.append(final)

json_object = json.dumps(entries, indent = 4)
    
with open("output.json", "w") as f:
	f.write(json_object)

