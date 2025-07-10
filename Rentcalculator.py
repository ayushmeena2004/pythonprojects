#house rent
#food cost
#Travelling cost
#electricity bill
#no. of person
while True:
    house_rent=float(input("Enter the House Rent:"))
    food_cost=float(input("Enter the Food Cost:"))
    Travel_cost=float(input("Enter the Travel Cost:"))
    elec_bill=float(input("Enter the Electricity bill:"))
    np=int(input("Enter the number of person:"))
    total_expense=house_rent+food_cost+Travel_cost+elec_bill
    per_person=total_expense/np
    print(f"Amount per person is: {per_person}")
    break