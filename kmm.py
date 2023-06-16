

print("print enter first number")
number_one = int(input())

print("enter number two")
number_two = int(input())

kmm = 0
x = 0

if number_one < number_two:
    x = number_one
else:
    x = number_two

for i in range (1, number_one+1):
    if number_one % i ==0 and number_two % i ==0:
        kmm = i

print(kmm)
