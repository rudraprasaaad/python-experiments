# int, str, tuple are immutable because these thing are mutable by object not by value
# we can re-assign to these variable when re-assgin the variable it points to different reference.


a = 10
print(id(a)) # id: 139798799914064
b = a
a = a + 5
print(id(a)) # id: 139798799914224

# if the a points to same object then it will have same id.

print(b)
print(a)

x = [1, 2, 3]
y = x
x.append(4)

print(f"Value of x are: {x}")
print(f"Value of y are: {y}")

# they're pointing to same object because list are immutable.

print(id(x)) # 140520123802496
print(id(y)) # 140520123802496

x = x + [5]
print(x)

i = 10
print(type(i))

i = "hello"
print(type(i))