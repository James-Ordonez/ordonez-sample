# INPUT SALARY
salary = int(input("Provide your current Monthly Salary:"))

if salary > 29999:
    print("You are eligible for a loan")
else:
    print("Not qualified for a loan because of low salary")

# INPUT LOAN

loan = int(input("Input amount of loan: "))

if loan > salary*10:
    print("Too high loan request")
else:
    months = int(input("How many months to pay: "))
    print("There is a 10%","interest increase")
    interest = loan*0.10
    print("Amount of loan to be paid back: ", loan+interest*months)