def counts(sen,pattern):
    count=0
    for i in sentence:
        if i==pattern:
            count+=1
    return(count)

sentence=input("Enter a sentence")
pattern=input("Enter the character to be counted")
result=counts(sentence,pattern)
print(result)
