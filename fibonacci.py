def fibo(n):
    a=0
    b=1
    for i in range(n):
        if i==0 or i==1:
            print(i)
        else:
            c=a+b
            print(c)
            a=b
            b=c

limit=int(input("enter the number of fibonaciees to be printer"))
result=fibo(limit)
print(result)

