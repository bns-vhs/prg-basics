parking_hours = int(input("How much would you like to spend on our parking?"))
if parking_hours <=2:
    print("5 PLN, please")
elif parking_hours <6:
    print("15 PLN, please")
elif parking_hours >=6:
    print("20PLN, please")