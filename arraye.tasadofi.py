
import random

n = int(input())

arra = []
tol_arra = 0

while tol_arra != n:
    x = random.randint(0, n)       
    if x in arra :
        arra.clear
    else:
        arra.append(x)  
        tol_arra = tol_arra + 1 
    
print(arra, end="")

