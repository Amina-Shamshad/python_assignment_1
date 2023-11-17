def ap(fun,seq,num):
    seq=sequence.split()
    print(seq)
    a=int(seq[0])
    print(a)
    d= int(seq[1])-int(seq[0])
    if fun=='sum':
       sum= (number/2)*(2*a+(number-1)*d)
       return(f'sum of the first {number} numbers of the given series is {sum}')
    elif fun=='nterm':
        nterm= a+(number-1)*d
        return(f'The Nth number of the given series is {nterm}')
    elif fun=='cdiff':
        return(f'The commond difference between the terms is {d}')

sequence= input("enter the sequence to be performed as string seperated by space ")
number=int(input("enter the nth number"))
func=input("function to be performed")
result=ap(func,sequence,number)
print(result)
