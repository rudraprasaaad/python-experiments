sugar_amount = 2
print(f"Initial Sugar: {sugar_amount}") 

print(f"ID of 2: {id(2)}")
print(f"ID of 2: {id(12)}")

numbers = set()
print(f"Initial numbers mix id: {id(numbers)}")
numbers.add(1)
numbers.add(1)
numbers.add("two")
print(numbers)
print(f"After numbers id: {id(numbers)}")