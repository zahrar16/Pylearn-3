print("print enter first number")
number_one = int(input())

print("enter number two")
number_two = int(input())

x = 0
bmm = 0

if number_one > number_two:
    x = number_one
else:
    x = number_two

for i in range(1, x+1):
    if number_one % i == 0 and number_two % i == 0:
        bmm = i

print(bmm)    