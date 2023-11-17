def gp(fun,seq,num):
    seq=sequence.split()
    print(seq)
    a=int(seq[0])
    print(a)
    r= int(seq[1])/int(seq[0])
    if fun=='sum':
       if r==1:
          sum= num*a
          return(f'sum of the first {number} numbers of the given series is {sum}')
       else:
           sum=a*((r**num)-1)/(r-1)
           return(f'sum of the first {number} numbers of the given series is {sum}')
    elif fun=='nterm':
        nterm= a*(r**(number-1))
        return(f'The Nth number of the given series is {nterm}')
    elif fun=='cratio':
        return(f'The commond difference between the terms is {r}')

sequence= input("enter the sequence to be performed as string seperated by space ")
number=int(input("enter the nth number"))
func=input("function to be performed")
result=gp(func,sequence,number)
print(result)