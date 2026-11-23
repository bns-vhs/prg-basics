categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
current_expense = 0
highest_expense = 0
for i in range(len(expenses)):
    current_expense = expenses[i]
    if current_expense > highest_expense:
        highest_expense = current_expense
print(highest_expense)