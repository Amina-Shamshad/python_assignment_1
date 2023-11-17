def guessGame(num1,num2,num3):
    import random
    val=random.randint(num1,num2)
    # print(val)
    if num3==val:
      return("correct")
    else:
      return("better luck next time")


num1=int(input('lower limit'))
num2=int(input('upper limit'))
num3=input("enter the gussed number")
result=guessGame(num1,num2,num3)
print(result)