

print("enter user number")
user_number = int(input())

for i in range(0,user_number):
    if i%2 == 0:
        print("*", end="")
    else:    
        print("#", end="")