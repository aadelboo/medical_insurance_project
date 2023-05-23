#create a empty dictionaries to store patients and their insurance costs
medical_costs = {}

#adding patients in dictionaries
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

#adding 3 patients in one line and print medical costs
medical_costs.update({"Connie": 8886.0, "Issac": 16444.0, "Valentina": 6420.0})
#print(len(medical_costs)) #uncomment to print

#update vinay costs and print the updated medical costs
medical_costs["Vinay"] = 3325.0
#print(medical_costs) #uncomment to print

#calculate average cost
total_costs = 0
for cost in medical_costs.values():
    total_costs += cost

average_cost = total_costs / len(medical_costs)
#print(f"Average Insurance Cost is: {average_cost}") #uncomment to print

#create a second dict that maps patient names and ages. then Zip the variables
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]
zipped_ages = zip(names, ages)

#create a new dictionnary using list comprehension and print it
names_to_ages = {names:ages for names, ages in zipped_ages}
#print(names_to_ages) #uncomment to print

#use .get on Marina and print it
marina_age = names_to_ages.get("Marina", None)
#print(f" Marina's age is {marina_age}") #uncomment to print

#create a dict to represent a database
#initialize a empty dict and add Marina Value
medical_records = {}
medical_records["Marina"] = {
    "Age": 27,
    "Sex": "Female",
    "BMI": 31.1,
    "Children": 2,
    "Smoker": "Non-smoker",
    "Insurance_cost": 6607.0
}

medical_records["Vinay"] = {
    "Age": 24,
    "Sex": "male",
    "BMI": 26.9,
    "Children": 0,
    "Smoker": "Non-smoker",
    "Insurance_cost": 3225.0
}

medical_records["Connie"] = {
    "Age": 43,
    "Sex": "Female",
    "BMI": 25.3,
    "Children": 3,
    "Smoker": "Non-smoker",
    "Insurance_cost": 8886.0}

medical_records["Isaac"] = {
    "Age": 35,
    "Sex": "male",
    "BMI": 20.6,
    "Children": 4,
    "Smoker": "Smoker",
    "Insurance_cost": 16444.0
}

medical_records["Valentina"] = {
    "Age": 52,
    "Sex": "Female",
    "BMI": 18.7,
    "Children": 1,
    "Smoker": "Non-smoker",
    "Insurance_cost": 6420.0
}
# print(medical_records) #uncomment to print

#access and print connie data
#print("Connie's insurance cost is " + str(medical_records["Connie"]["Insurance_cost"]) + " dollars.") #uncomment to print

#remove vinay from medical records
medical_records.pop("Vinay")

#iterate through medical records and print each record
for name, record in medical_records.items():
    #print(name + " is a " + str(record["Age"]) + " year old, " + record["Sex"] + ", " + record["Smoker"] + " with a BMI of " + str(record["BMI"]) + " and insurance cost of " + str(record["Insurance_cost"])) #uncomment to print
