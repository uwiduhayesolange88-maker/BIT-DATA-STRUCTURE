Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

# Project 116: Retail Discount Calculator

from array import array

print("=== Retail Discount Calculator ===")

# -------------------------------
# Integers Section
# -------------------------------
# Let's say these are quantities of items purchased
quantities = [5, 8, 3, 12, 7]

total = sum(quantities)
average = total / len(quantities)
minimum = min(quantities)
maximum = max(quantities)

print("\n--- Integers Section ---")
print(f"Quantities: {quantities}")
print(f"Total: {total}, Average: {average:.2f}, Min: {minimum}, Max: {maximum}")

# -------------------------------
# Strings Section (Formatted Report)
# -------------------------------
print("\n--- String Report ---")
report = (
    f"Retail Discount Report\n"
    f"Total Items Purchased: {total}\n"
    f"Average Quantity per Purchase: {average:.2f}\n"
)
print(report)

# -------------------------------
# Booleans Section
# -------------------------------
print("\n--- Boolean Check ---")
threshold = 6
# Compound condition: check both average and max
if average > threshold and maximum > 10:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# -------------------------------
# Lists Section
# -------------------------------
print("\n--- Lists Section ---")
items = ["Shoes", "Shirt", "Hat", "Socks"]

print("Original List:", items)

# Add a new element
items.append("Jacket")
print("After Adding Jacket:", items)

# Remove an element based on a condition (remove "Hat")
if "Hat" in items:
    items.remove("Hat")
print("After Removing Hat:", items)

# Sort the list
items.sort()
print("After Sorting:", items)

# -------------------------------
# Arrays Section
... # -------------------------------
... print("\n--- Arrays Section ---")
... # Create array of first 3 quantities
... arr = array("i", quantities[:3])
... print("Array Contents:", arr)
... 
... # Compute sum of array
... array_sum = sum(arr)
... print("Sum of Array:", array_sum)
... 
... # Compare with list sum
... print("Compare Array Sum with List Sum:")
... print("Equal?" , array_sum == sum(quantities[:3]))
... 
... # -------------------------------
... # Dictionaries Section
... # -------------------------------
... print("\n--- Dictionaries Section ---")
... records = [
...     {"id": 1, "name": "Shoes", "value": 50},
...     {"id": 2, "name": "Shirt", "value": 30},
...     {"id": 3, "name": "Hat", "value": 20},
... ]
... 
... print("Original Records:", records)
... 
... # Update one record (change Shirt value)
... records[1]["value"] = 35
... 
... # Delete another (remove Hat)
... records = [r for r in records if r["id"] != 3]
... 
... # Compute total of 'value'
... total_value = sum(r["value"] for r in records)
... 
... print("Updated Records:", records)
... print("Total Value of Records:", total_value)
... 
... print("\n=== End of Project 116 ===")
