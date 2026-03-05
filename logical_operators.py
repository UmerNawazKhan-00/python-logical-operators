# Logical Operators in Python: AND, OR, NOT

a = 10
b = 5

# NOT operator
print(not False)
print(not (a > b))  # a > b is True, but NOT makes it False

# AND operator
val1 = True
val2 = True
print("AND operator:", val1 and val2)  # True only if both are True

# OR operator
val1 = True
val2 = False
print("OR operator:", val1 or val2)  # True if at least one is True
