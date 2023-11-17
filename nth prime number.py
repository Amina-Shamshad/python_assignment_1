
def nth_prime(n):
    lst=[]
    for i in range(2,n+1):
        flag=0
        for j in range(2,i//2+1):
            if i%j ==0:
                flag=1
                break
        if flag==0:
            lst.append(i)
    return(lst)

limit= int(input("enter the nth number"))
result=nth_prime(limit)
print(result)