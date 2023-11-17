def factorial(n):
    if limit<=0:
        print(1)
    else:
        result=1
        for i in range(n,1,-1):
            result=result*i
        print (result)
def nth_fact(n):
 for j in range(n):
       factorial(j)
limit=int(input("enter the limit of  numbers to be print as factorial"))
result=nth_fact(limit)
print(result)
