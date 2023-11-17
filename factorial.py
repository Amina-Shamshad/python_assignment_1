def factorial(n):
    if limit<=0:
        return 1
    else:
        result=1
        for i in range(limit,1,-1):
            result=result*i
        return result

limit=int(input("enter the number to be print as factorial"))
results= factorial(limit)
print(results)
