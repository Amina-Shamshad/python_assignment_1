def swap_case(s):
    lst=[]
    for i in s:
        if i.isupper():
            i=i.lower()
            lst.append(i)
        else:
            i=i.upper()
            lst.append(i)
    return (''.join(lst).replace(',',''))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)