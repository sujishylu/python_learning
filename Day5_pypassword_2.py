import random
import string

numeric = [] # create a list so that if can be shuffled
alpha =[]
special_ch =[]
password =[]
final_password =""
for i in string.printable:
    if i.isalpha():
        alpha.append(i)
    elif i.isnumeric():
        numeric.append(i)
    elif not i.isalpha() or i not in string.whitespace:
        special_ch.append(i)
alpha_le = input("  how many alpha char you want ")
special_le = input(" how many special_ch ")
numeric_le = input(" how many numeric ch you want ")
for i in range(0,int(alpha_le)):
    password += random.choice(alpha)
for i in range(0,int(numeric_le)):
    password += random.choice(numeric)
for i in range(0,int(special_le)):
    password += random.choice(special_ch)
random.shuffle(password)
print("your password is = ", final_password.join(password))


