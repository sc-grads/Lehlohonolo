from typing import Dict

money: dict[str, float | int] = {
    'bank': 8564.61,
    'paypal': 1998.21,
    'cash': 480,
    'payoneer': 250.5
}

# First solution using a for loop
total_amount = 0
for value in money.values():
    total_amount += value

print(total_amount)

# Second solution using the sum() function and the dictionary.values() method
total_amount = sum(money.values())
print(total_amount)
