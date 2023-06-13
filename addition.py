def add(a, b):
    return a + b


print(add(1, 2), '\n', type(add(1, 3)))
# Number and mathematical operations
a = 1
A = 'suji'
b = 1.0
c = 1j
d = -12
print(str(a) + " is " + str(type(a)))  # o/p: 1 is <class 'int'>
print(a+b)  # o/p: 2.0
print(type(b))  # o/p: float
print(type(c))  # o/p : Complex
print(type(d))  # o/p : int
print((float(a)))  # o/p: 1.0
print(A)  # 0/p : suji -- identifiers are case sensitve 

#add
print(10/20)  # o/p: 0.5
print(10//20)  # o/p : 0 - flooring nearest floating point
print(2**3)    # o/p : 8 - power
print(3%2)  # o/p : 1 --reminder
