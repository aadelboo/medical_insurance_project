# Create calculate_insurance_cost() function below:
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars")
    return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(name= "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)

# Estimate Omar's insurance cost
omar_insurance_cost = calculate_insurance_cost(name= "Omar", age=35, sex=1, bmi=22.2, num_of_children=0, smoker=1)

# Second functions to calculate the differences between Omar and Maria
def diff_insurance(first_insurance_cost, second_insurance_cost):
    diff_cost = first_insurance_cost - second_insurance_cost
    print("The difference in insurance cost is " + str(diff_cost) + " dollars")
    return diff_cost

diff_insurance(omar_insurance_cost, maria_insurance_cost)
