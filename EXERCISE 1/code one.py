Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Project 116: Retail Discount Calculator

import array

print("=== Retail Discount Calculator ===\n")

# ------------------------------
# Integers: Quantities, compute total, average, min, max
# ------------------------------
quantities = [10, 15, 20, 5, 30]  # example item quantities purchased
total_qty = sum(quantities)
avg_qty = total_qty / len(quantities)
min_qty = min(quantities)
max_qty = max(quantities)

print("Quantities:", quantities)
print(f"Total Quantity: {total_qty}")
print(f"Average Quantity: {avg_qty:.2f}")
print(f"Minimum Quantity: {min_qty}, Maximum Quantity: {max_qty}\n")

# ------------------------------
# Strings: Formatted report
# ------------------------------
report = (
    f"Retail Discount Calculator Report\n"
    f"Total Quantity Sold: {total_qty}\n"
    f"Average Quantity per Item: {avg_qty:.2f}\n"
)
print(report)

# ------------------------------
# Booleans: Apply threshold condition
# ------------------------------
threshold = 12
if avg_qty > threshold and max_qty > 25:   # compound condition
    print("Status: Above Standard ✅")
else:
    print("Status: Below Standard ⚠️")
print()

# ------------------------------
# Lists: Maintain and modify
# ------------------------------
items = ["Shirt", "Shoes", "Cap", "Jacket"]
... print("Original Items List:", items)
... 
... 
... items.append("Bag")
... 
... if "Cap" in items:
...     items.remove("Cap")
... 
... items.sort()
... 
... print("Modified & Sorted Items List:", items)
... print()
... 
... 
... #
... arr = array.array('i', [10, 15, 20])  
... arr_sum = sum(arr)
... list_sum = sum([10, 15, 20])
... 
... print("Array values:", arr.tolist())
... print("Sum from Array:", arr_sum)
... print("Sum from List:", list_sum)
... print(f"Comparison Match? {arr_sum == list_sum}
... 
... records = [
...     {"id": 1, "name": "Shirt", "value": 100},
...     {"id": 2, "name": "Shoes", "value": 200},
...     {"id": 3, "name": "Jacket", "value": 300},
... ]
... 
... print("Original Records:", records)
... 
... 
... records[0]["value"] = 
... 
... 
... records = [rec for rec in records if rec["id"] != 2]
... 
... 
... total_value = sum(rec["value"] for rec in records)

print("Updated Records:", records)
print(f"Total Value of Remaining Records: {total_value}")
