# Lesson - for loop concept

'''height_list = [199, 220, 200]
length = len(height_list)
sum1 = 0
#input("sutenet heights")
#student_h= input("sutenet heights").split()

for i in height_list:
    sum1 = sum1 + i
print ("average = " , sum1/length)
total =  sum(height_list)
print("average =" , total)



height_list_1 = [199, 220, 200]
total = sum(height_list_1)
print("Sum =", total)'''
#frizzbuzz
'''end = input(" give the end number")
for i in range ( 1, int(end)+1):
    if i%3 == 0 or  i%5 == 0 :
        print ("frizzbuzz")
    else:
        print ( i )'''
# generate password
import string
import random
integer = []
special_char = []
alphabet = []
for i in range(0,10):
    integer.append(i)
for a in string.printable:
    if not a.isalnum() and a not in string.whitespace:
        special_char.append(a)
for s in string.printable:
    if s.isalpha():
        alphabet.append(s)
alpha_le = input("  how many alpha char you want ")
special_le= input ( " how many special_ch ")
numeric_le = input (" how many numric ch you want ")
password1 =""
password2=""
password=""
a_c = []
n_c = []
s_c = []
for i in range(0,int(alpha_le)):
    r=random.randint(0,24)
    a_c.append(alphabet[r])
password =password.join(a_c)

for i in range(0,int(numeric_le)):
    r=random.randint(0,9)
    n_c.append(str(integer[r]))
password1 = password1.join(n_c)
print(" your password = ", password1)
for i in range(0,int(special_le)):
    r=random.randint(0,len(special_char))
    s_c.append(str(special_char[r]))
password2 =password2.join(s_c)
print(" your passowrd = ", password2)
print("your final password = ", password+password1+password2)




