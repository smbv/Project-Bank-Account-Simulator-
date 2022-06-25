Acc_name = input("What is the name of your new account? ")
Balance = float(input("What will your starting balance be? "))

user_selection = 0
times_deposit = 0
total_deposit = 0
times_withdrawal = 0
total_withdrawal = 0
times_wrong_withdrawal = 0
total_wrong_withdrawal = 0
fees = 5 
times_fees = 0
total_fees = 0

while user_selection != "3": #main loop 
  print("\n Account: ", Acc_name, "\n Balance: ", Balance, "\n 1) Deposit some funds. ", "\n 2) Withdraw some funds.", "\n 3) Quit. ", "\n Please select one option")
  user_selection = input("Enter your selection: ")

  if user_selection == "1": #option 1
   Deposit = float(input("Enter the amount you would like to deposit: "))
   Balance = Balance + Deposit 
   times_deposit += 1
   total_deposit += Deposit
   print(Balance)

  elif user_selection == "2": #option 2  
    Withdrawal = float(input("Enter the amount you would like to withdraw: "))
    if Balance < Withdrawal:  #fees 
      print("Insufficient Funds. Five dollars will be deducted from your balance as a penalty. Have a nice day!")
      Balance -= fees
      times_wrong_withdrawal += 1
      total_wrong_withdrawal += Withdrawal
      times_fees += 1
      total_fees += fees
      print(Balance)
    else:
      Balance = Balance - Withdrawal 
      times_withdrawal += 1
      total_withdrawal += Withdrawal
      print(Balance)
      
  elif user_selection == "3": #option 3 
    print("\nAccount: ", Acc_name, "\n Balance: ", Balance, times_deposit, "\n Deposits totaling", total_deposit, times_withdrawal, "\n Withdrawals totaling", total_withdrawal, times_wrong_withdrawal, "\n Wrong withdrawals totaling", total_wrong_withdrawal, times_fees, "\n Fees totaling", total_fees)
  else:
    print("Invalid choice. Try again.")