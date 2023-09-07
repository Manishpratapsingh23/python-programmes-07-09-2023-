# Python program to find those numbers which are divisible by d and multiples of m, between x and y (both included).
x=int(input("enter first limit: "))
y=int(input("enter last limit: "))
d=int(input("enter divisor: "))
m=int(input("enter multiple number: "))
for i in range(x,y+1):
    if i%d==0:
        if i%m==0:
            print(i)


            
#output:

            
#enter first limit: 1
#enter last limit: 140
#enter divisor: 7
#enter multiple number: 5
#35
#70
#105
#140
