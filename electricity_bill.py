def calculate_bill(units):
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = 100*3 + 100*5 + (units - 200) * 7

    return bill

print("SMART ELECTRICITY BILL CALCULATOR")  

units = float(input("Enter electricity units used:"))

if units <0:
    print("Please enter vaild units.")
else:
    bill = calculate_bill(units)

    print("\n----- YOUR BILL-----")
    print("Units Consumed:", units)
    print("Estimated bill: $",bill)

    if units > 200:
        print("Tip: Save electricity by switching off unused applications!")
    else:
        print("Tip: Great! Keep saving electricity.")

