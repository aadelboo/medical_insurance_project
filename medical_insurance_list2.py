names = [
    "Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily",
    "Nikita", "Paul"
]
insurance_costs = [
    13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0,
    12064.0
]

# Add your code here

# Append a new individual, "Priscilla", to names and 8320.0 to insurance_costs.
names.append("Priscilla")
insurance_costs.append(8320.0)

# Create a new variable called medical_records that combines insurance_costs and names into a list using the zip() function.
medical_records = list(zip(insurance_costs, names))
print(medical_records)

# Print out medical_records in order to see the list.
num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records")

# Select the first medical record in medical_records, and save it to a variable called first_medical_record.
first_medical_record = medical_records[0]
print("Here is the first medical record: " + str(first_medical_record))

# Sort the medical records alphabetically by name
medical_records.sort()
print("Here are the medical records sorted by insurance cost: " +
      str(medical_records))

# The three cheapest insurance costs in our medical records
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records : " +
      str(cheapest_three))

# The three most expensive insurance costs in our medical records
priciest_three = medical_records[-3:]
print(
    "Here are the three most expensive insurance costs in our medical records: "
    + str(priciest_three))

# Count the number of occurrences of "Paul" in our medical records list, and store the result in a variable called occurrences_paul.
occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) +
      " individuals with the name Paul in our medical records.")

# Sort the medical records alphabetically by name
medical_records_alpha = sorted(list(zip(names, insurance_costs)))
print("This time the list is alphabetically sorted: " +
      str(medical_records_alpha))

# The middle five records
middle_five_records = medical_records[3:8]
print(middle_five_records)
