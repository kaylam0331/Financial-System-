'''
Kayla Mabalot | (@026840318)
23 October 2023 
IS 340, Project 2 | Fall 2023
______________________________
Coding Prompt:
HalloWeen Town has hired you to create software for CromWell's Fargo banking system. You have been tasked to create:
- New Credit Card Application Module
- New Monthly Loan Payment Calculator
- New IRA Maturity Value Calculator
'''
import math # calculator
maxIR = 0.185 #Global Var: Max. IR | State Law
def Main():
  print("\n______________________________\nHalloWeen Town's...\nCromWells' Fargo\n")
  while True:
    choice = Menu() # Display Menu
    if choice == '1':
      return ApplyForCard()
      Menu()
    elif choice == '2':
      return PassThePayment()
      Menu()
    elif choice == '3':
      return GrowWithMaturity()
      Menu()
    elif choice == 'q':
      print("EXIT.")
      loop = False
    else:
      print(f"{choice} is not a valid choice. Try Again.")
  print("______________________________\nThank you for banking with CromWells' Fargo...Brewing since 1998!")
#Main Function
def Menu():
  print("______________________________\n (1) Apply W/ Aggie: Credit Cards\n (2) Plan W/ Piper: Loan Payment\n (3) Seek W/ Sophie: IRA Growth Values \n (Q) Quit")
  choice = input("Enter Choice: #")
  return choice
#Menu Function
def ApplyForCard(): #Credit Card info - Option #1 
  acc = float(input("______________________________\n(1) Apply With Aggie:\nChecking Account Balance: $ ")) 
  # Checking Account:
  if acc > 0:
    print("Balance of: $", "%.2f" % round(acc,2)) #Validate Positive Number
  elif acc < 0:
    print("Balance of: A Negative Number... Try Again Next Month!")
  # Credit Card:
  x = float(acc)
  if x > 15000: #$15K or more
    print("(1) Platnium: You are eligible for a Platnium Card!\nCode: #777") #ApprovalCode
  elif x > 10000: #$10K or more
    print("(2) Gold: You are eligible for a Gold Card!\nCode: 444") #ApprovalCode
  elif x > 5000: #$5K or more
    print("(3) Silver: You are eligible for a Silver Card!\nCode: 333") #ApprovalCode
  elif x < 5000:
    print("(0) Not Approved: You cannot apply for a credit card with this balance.")
    # UI: Credit Card
  Main()
#Credit Card Function
def PassThePayment(): #Loan Payment info - Option #2
  n = int(input("______________________________\n(2) Plan With Piper:\nEnter Years until Loan Maturity:")) #Years: N
  if n < 0: #Validation Input
    print("Years cannot be negative. Try Again.")
  else:
    print(n,"years") #Default Argument
  p = float(input("Enter Loan's Principal Amount: $ ") )#Principal Amount: P
  if p < 0: #Validation Input
    print("Amount Must be Greater than 0. Try Again.")
  else:
    print("$","%.2f" % round(p,2))
  r = float(input("Enter the Anual Interest Rate: % ")) #Interest Rate: R
  if r < 0: #Validation Input
    print("Rate Must be Positive. Try Again.")
  print(n, "years |", "$", "%.2f" % round(p,2), "|", r, "%") # UI: Loan 
  CalcThePayment(p,r,n) #Pass data: p, r, n #Return result back to main
#Loan Payment Function
def CalcThePayment(p,r,n): #Payment Plan Calculator
  print(p,r,n)
  #Arguments of function:
  LoanAmt = float(333333)
  r = float(.03) #Interest Rate R
  n = int(30) #UserInput(Num of Years n: default: 30)
  #Work of function:
  r = 4.5 #Assume User Input
  IR = float(r/100) #Divide r by 100 for IR
  MR = IR/12 #Divide IR by 12 for MonthlyRate
  #Calculations
  M = (LoanAmt * MR) / (1 - math.pow((1 + MR),(-12 * n)))#Equation = Monthly Payment M
  #Calculator: How Much I Pay Per Month
  print("Monthly Payment Due: $", "%.2f" % round(M,2))
  Main()
#Calculator for Loan
def GrowWithMaturity(): #IRA info - Option #3
  currentAge = int(input("______________________________\n(3) Seek With Sophie:\nEnter current age: "))
  print("You are:", currentAge, "years old.")
  if currentAge < 65:
    print("Congrats","you are eligible for a ROTH IRA!")
  elif currentAge < -1:
    print("Please enter a valid age.")
  else:
    print("Oops! You are not eligible for a ROTH IRA.")   
  N = (65 - currentAge)
  D = input("Enter Amount of Annual Deposit: $")
  R = input("Enter Annual Interest Rate: %")
  print(N, D, R)# UI: IRA
  CalcTheGrowth(N,D,R) #Pass data: n, d, r #Return result back to main
#Roth IRA Function
def CalcTheGrowth(N,D,R):
  YearsUntilMaturity = int(21)
  AnnualDepositAmt = float(21000.34)
  InterestRate = float(3.33) # Arguments of Calculator for IRA
  r = 4.5 #UI: Interest Rate
  IR = r/100 #AnnualInterestRate
  M = AnnualDepositAmt * ( (math.pow((1 + IR), YearsUntilMaturity ) - 1) / r)
  print("Maturity Value of IRA: $", "%.2f" % round(M,2))
  Main()
#Calculator for IRA
  
  

Main()