def checkodd(n):
    if number%2==0:
        return(f'The given number is EVEN')
    else:
        return(f'The given number is ODD')

number=int(input("enter the number to be checked"))
result= checkodd(number)
print(result)