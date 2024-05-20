import math

#ask for users choice for investment or bond
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
choice = input("Which option would you like to choose? ")

#if statement for typing any form of investment
if choice == "investment" or choice == "Investment" or choice == "INVESTMENT":
    #asking user for investment details and storing as variables
    P = int(input("How much would you like to deposit in £? "))
    t= int(input("How many years do you wish to invest for? "))
    r= int(input("What is the interest rate in %? "))
    r=r/100
    #asking user for which type of investment
    interest=input("Do you want simple or compound interest? ")
    #if statement for calculating and dispalying simple interest
    if interest =="simple":
        A = P *(1 + r*t)
        print(f"Your total after {t} years will be £{(round(A,2))}")
    #else if statement for calculating and displaying compound interest 
    elif interest == "compound":
        A = P * math.pow((1+r),t)
        print(f"Your total after {t} years will be £{(round(A,2))}")
    #else statement to display error for user not writing compound or simple
    else:
        print("ERROR: Invalid input")

#else if statement for typing any form of bond
elif choice == "bond" or choice == "Bond" or choice == "BOND":
    #asking user for bond details and storing as variables
    P = int(input("What is the present value of the house in £? "))
    i= int(input("What is the annual interest rate in %? "))
    i=((i/100)/12)
    n = int(input("What is the number of months you plan to take to repay the bond? "))
    #calculating and displaying bond repayments
    repayment = (i * P)/(1 - (1 + (i))**(-n))
    print(f"You will have to pay £{(round(repayment,2))} each month")
#else statement to display error for user not typing any form of bond or investment
else:
    print("ERROR: Invalid input")
