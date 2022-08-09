#inputs and variables

bill = float(input("How much did your meal cost? "))

tip = int(input("how much tip do you want to add 15% , 18% or 20% ?? "))

tax = 0.05

#math calculations

tax_amt = bill * tax

tip_amt = bill * tip/100

total = bill + tip_amt + tax_amt

#printing

print(f"Your Bill is ${bill:.2f} and your tip is ${tip_amt:.2f} ")

print(f"Your total with tax is ${total:.2f}")



##input data
#Bill_Amount = input("Enter the bill amount- ")
#Bill_AmountDigit = ""
#Bill_AmountCurrency = ""

##iterates through the Bill Amount Entered and seperates the Currency and Numbers
#for i in range(0, len(Bill_Amount)):
    #if Bill_Amount[i].isdigit() == True:
        #Bill_AmountDigit=Bill_AmountDigit+Bill_Amount[i]
    #else:
        #Bill_AmountCurrency=Bill_AmountCurrency+Bill_Amount[i]
        
##Calculate Tips
#tip1= 0.15*int(Bill_AmountDigit)
#tip2= 0.18*int(Bill_AmountDigit)
#tip3=0.2*int(Bill_AmountDigit)

#Prints the Different Tips
#print(f"""You can give the following Tips for the Bill Amount:
#i) {Bill_AmountCurrency}{tip1:.2f}
#ii) {Bill_AmountCurrency}{tip2:.2f}
#iii) {Bill_AmountCurrency}{tip3:.2f}""")









# Write a script that takes a dollar amount and recommennds a tip (15%, 18% and 20%)

#total = float(input("What is you're bill sub-total? ").strip('$'))

#tip_15 = total * 0.15
#tip_18 = total * 0.18
#tip_20 = total * 0.20

#print("Tip Suggestions:")
#print("----------------")
#print(f"15% is ${tip_15:.2f}")
#print(f"18% is ${tip_18:.2f}")
#print(f"20% is ${tip_20:.2f}")