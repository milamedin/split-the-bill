print("Welcome to the Bill Calculator")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))/100
people = int(input("How many people to split the bill: "))
x = round((bill + bill*tip)/people, 2)
print(f"Each person should pays ${x}")
