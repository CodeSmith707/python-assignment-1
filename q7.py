# 7.	Given list of items purchased in a file display the following: 
# No of items purchased, No of free items, Amount to pay, Discount given, Final amount paid
# Concepts: files, dictonary

# Sample output for purchase-1.txt file:
# No of items purchased: 5 
# No of free items: 2
# Amount to pay: 485
# Discount given: 80
# Final amount paid: 405

file = open("purchase-1.txt", "r")
lines = file.readlines()
file.close()

items = []
prices = []
discount_per_item = 0

for line in lines:
    line = line.strip()
    if line == "":
        continue
    if line.startswith("Discount"):
        parts = line.split()
        discount_per_item = int(parts[1])
    else:
        parts = line.split()
        item_name = parts[0]
        item_price = int(parts[1])
        items.append(item_name)
        prices.append(item_price)

num_items = len(items)
num_free_items = 0
amount_to_pay = sum(prices)
discount_given = num_items * discount_per_item
final_amount = amount_to_pay - discount_given

print("No of items purchased:", num_items)
print("No of free items:", num_free_items)
print("Amount to pay:", amount_to_pay)
print("Discount given:", discount_given)
print("Final amount paid:", final_amount)

