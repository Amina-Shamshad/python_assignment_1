def prime(n):
    flag=0
    for j in range(2,num//2+1):
        if num%j ==0:
            flag=1
            break
    if flag==0:
        return(f'{num} is a prime number')
    else:
        return(f'{num} is not a prime number')

num=int(input("enter the number to be checked"))
result=prime(num)
print(result)