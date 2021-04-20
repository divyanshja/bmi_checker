import json

def calBMI(mass,height):
	bmi = mass/height
	return  "{:.2f}".format(float(bmi))


def bmicategory(bmi):
	if float(bmi) <= 8.4:
		return "Underweight"
	elif float(bmi) >= 18.5  and float(bmi) <= 24.9:
	    return "Normalweight"
	elif float(bmi) >= 25 and float(bmi) <=29.9:
	     return "Overweight"
	elif float(bmi) >= 30 and float(bmi) <= 34.9:
	      return "Moderately obese"
	elif float(bmi) >= 35 and float(bmi) <= 39.9:
	      return "Severely obese"
	else :
	      return "very Severely obese"



def healthrisk(bmi):
	if float(bmi) <= 8.4:
		return "Malnutrition risk"
	elif float(bmi) >= 18.5 and float(bmi) <= 24.9:
	    return "Low risk"
	elif float(bmi) >= 25 and float(bmi) <=29.9:
	     return "Enhanced risk"
	elif float(bmi) >= 30 and float(bmi) <= 34.9:
	      return "Medium risk"
	elif float(bmi) >= 35 and float(bmi) <= 39.9:
	      return "High risk"
	else:
	      return "Very High risk"



def overweight(bmicategory):
	if bmicategory == 'Overweight':
		return 'True'






