medical_data = \
"""Marina Allison   ,27   ,   31.1 ,
#7010.0   ;Markus Valdez   ,   30,
22.4,   #4050.0 ;Connie Ballard ,43
,   25.3 , #12060.0 ;Darnell Weber
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1
,#3022.0   ;   Vinay Padilla,24,
26.9 ,#4620.0 ;Meredith Santiago, 51   ,
29.3 ,#16330.0;   Andre Mccarty,
19,22.7 , #2900.0 ;
Lorena Hodson ,65, 33.1 , #19370.0;
Isaac Vu ,34, 24.8,   #7045.0"""

#replace all the # with €
updated_medical_data = medical_data.replace("#", "€")

#initialize variable to 0
num_records = 0

#count how many records there is and print it
for record in updated_medical_data:
    if record == "€":
        num_records += 1
print(f"There are {num_records} medical records in the data.")

#split the string into a list
medical_data_split = updated_medical_data.split(";")
#print(medical_data_split) #uncomment to see the list

#split the list into a list of lists to make it more readable
medical_records = []
for medrec in medical_data_split:
    medical_records.append(medrec.split(","))
#print(medical_records) #uncomment to see the list

#clean the data from spaces and add it to a new list.
medical_records_clean = []
for clean in medical_records:
    record_clean = []
    for item in clean:
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean)
#print(medical_records_clean) #uncomment to see the list

#capitalize the names
for record in medical_records_clean:
    record[0] = record[0].upper()
    #print(record[0]) #uncomment to see the list

#intialize empty lists for every element of medical_records_clean
names = []
ages = []
bmis = []
insurance_costs = []

#append the elements of medical_records_clean to the empty lists
for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])

#print(f"names: {names}") #uncomment to see the list
#print(f"ages: {ages}") #uncomment to see the list
#print(f"bmis: {bmis}") #uncomment to see the list
#print(f"insurance_costs: {insurance_costs}") #uncomment to see the list

#sum the bmis and convert them to float
total_bmi = 0
for bmi in bmis:
    total_bmi += float(bmi)

#calculate the average bmi
average_bmi = round(total_bmi / len(bmis), 2)
print(f"The avergae BMI is {average_bmi}")

#sum the insurance costs and convert them to float
total_insurance_costs = 0
for ins in insurance_costs:
   total_insurance_costs += (float(ins[1:])) #remove the € sign

#calculate the average insurance costs
average_insurance_costs = round(total_insurance_costs / len(insurance_costs), 2)
print(f"The average insurance cost is {average_insurance_costs} €")
