#Get the loan details
Amount_owed = float(input("How much money do you owe in dollars ?\n "))
apr = float(input("Enter the annual interest rate:"))
payment = float(input("what will be your monthly payment be, in dollars? \n"))
months = int(input("How many months do you want to see results for?\n"))

# Calculating monthly rate
monthly_rate = apr/100/12

for i in range(months):
    #Add in interest
    interest_paid = Amount_owed*monthly_rate
    Amount_owed = Amount_owed + interest_paid
    if Amount_owed-payment < 0:
        print("You paid off the loan in ", i+1, "months\n")
        break
    #After payment
    Amount_owed = Amount_owed - payment
    print("Paid", payment, " of which", interest_paid, "was interest", end=' ')
    print("Now I Owe", Amount_owed)

