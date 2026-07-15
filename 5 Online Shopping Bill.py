amount = float(input("Enter purchase amount: "))
if amount < 1000:
    discount = amount * 0.10
else:
    discount=0
gst=0.18*(amount-discount)
total_bill=amount-discount+gst
print("Purchase amount: ", amount)
print("Discount: ", discount)
print("GST: ", gst)
print("Total bill amount: ", total_bill)   
