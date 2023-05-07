names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

#initialize a new variable
total_cost = 0

#itireating trough the first list and add value to total_cost
for cost in actual_insurance_costs:
    total_cost += cost

#calculate and print the avg cost
average_cost = total_cost / len(actual_insurance_costs)
print("The average insurance cost: ", average_cost, " dollars.")

#iterate trough the list names and print information on the situation and one based on the condition
for i in range(0, len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars")
    if insurance_cost > average_cost:
        print("The insurance cost for " + name + " is above average.")
    elif insurance_cost < average_cost:
        print("The insurance cost for " + name + " is below average.")
    else:
        print("The insurance cost for " + name + " is equal to the average.")

#updated and print estimate costs
updated_estimated_costs = [update * 11/10 for update in estimated_insurance_costs]
print(updated_estimated_costs)

#extra challenge

#transform the first for loop into a while
while cost < len(actual_insurance_costs):
    total_cost += cost

print(total_cost)

#calculate how far the user is above or bellow the average
for i in range(0, len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    #difference_cost = insurance_cost - average_cost
    if insurance_cost > average_cost:
        print("The extra cost for " + name +
        " between the actual and average insurance cost is: "
        + str(insurance_cost - average_cost) + " €")
    elif insurance_cost < average_cost:
        print("The benefit for " + name +
        " between the actual and average insurance cost is: "
        + str(average_cost - insurance_cost) + " €")
    else:
        print("You pay the right price. There is no difference!")
