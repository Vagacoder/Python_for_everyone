#sc22

balance = 100
amount = 200

try:
    if amount > balance:
        raise ValueError("Amount exceeds balance")

except ValueError as except1:
    print(str(except1))

balance = balance - amount