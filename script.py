#create the initial variable
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

#insurance estimate formula that will be use to calculate the cost
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

#reasign a new value to AGE, calculate the difference and print it
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

#reasign a new value to BMI, calculate the difference and print it
age -= 4
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is "+ str(change_in_insurance_cost)+ " dollars.")

#reasign a new value to SEX, calculate the difference and print it
bmi -= 3.1
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost)+ " dollars.")

#reasign a new value to SMOKER, calculate the difference and print it
sex = 0
smoker = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for a man smoking instead of female is " + str(change_in_insurance_cost) + " dollars.")

#reasign a new value to NUM_CHILDREN, calculate the difference and print it
smoker = 0
num_of_children -= 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for a women who have 1 child instead of 3 is " + str(change_in_insurance_cost) + " dollars.")
