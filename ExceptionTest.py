# Test try/final/except

try:
    print("This is before raising exception.")
    a = 10.0 / 0.0
    print("This is after raising exception.")

# except Exception:
#    print("Divided by zero!")

finally:
    print("this is inside finally.")

print("this is after try")
