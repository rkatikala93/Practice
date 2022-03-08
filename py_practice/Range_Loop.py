expenses = []
num = int(input("Enter the number of expenses: "))
for i in range(num):
    expenses.append(float(input("Enter an expense: ")))
total_expenses = sum(expenses)
print("Total Expenses for the entire week : $", total_expenses, sep='')
#New comment to check the merge changes