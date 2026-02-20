# Program to calculate total cost of 3 items
# Apply 10% discount if total is greater than $50

# Accept price inputs from user
price1 = float(input("Enter price of item 1: "))
price2 = float(input("Enter price of item 2: "))
price3 = float(input("Enter price of item 3: "))

# Calculate total cost
total = price1 + price2 + price3

# Initialize discount
discount = 0

# Check if discount is applicable
if total > 50:
    discount = total * 0.10   # 10% discount

# Calculate final amount
final_amount = total - discount

# Display results
print("\n----- BILL DETAILS -----")
print("Original Total: $", total)

if discount > 0:
    print("Discount (10%): $", discount)
else:
    print("Discount: $ 0")

print("Final Amount to Pay: $", final_amount)