print('Welcome to the Tip Calculator')
bill = float(input('What was the total bill? $'))
ppl  = int(input('How many people to split the bill? '))
tip = float(input("What %age tip to add? "))
res = round(bill*(1+tip/100)/ppl,2)
print(f"Each person should pay ${res:.2f}")
