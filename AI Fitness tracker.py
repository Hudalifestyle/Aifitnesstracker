weight = flaot(int("Enter your weight?"))
bmi= flaot(int("Enter your BMI?"))
fat= flaot(int("Enter you fat precent?"))
import math
# bmi BMI = (pounds/inches^2) x 703.
def bmi_preceng(weight,height):
    BMI=(weight//(height)**2)*703
    bmi=round(BMI,2)
    return bmi
# fat
    # Men Body Fat Percentage = (1.20 x BMI) / (0.23 x Age) – 16.2.
    # Women Body Fat Percentage = (1.20 x BMI) / (0.23 x Age) – 5.4.
    # Body Fat Percentage Ranges.
def fat_precenge(bmi,age):
    #if geder men then
        # Men Body Fat Percentage = (1.20 x BMI) / (0.23 x Age) – 16.2.
        #print # Body Fat Percentage Ranges.
     #else:
        # Women Body Fat Percentage = (1.20 x BMI) / (0.23 x Age) – 5.4.
        #print# Body Fat Percentage Ranges.
def store():
    #store bmi
    #store fat
    #store weight
    #store date
def retrieve(list1):
    #retrieve bmi
    #retrieve fat
    #retrieve weight
    #retrieve date

