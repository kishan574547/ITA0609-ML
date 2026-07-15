balance=5000
pin=123
entered_pin=int(input("Enter your pin: "))
if entered_pin==pin:
    amount=float(input("Enter the amount to withdraw: "))
    if amount<=balance:
        balance-=amount
        print("Withdrawal successful. New balance: ", balance) 
    else:
        print("Insufficient balance.")
else:
    print("Invalid PIN.")
        
