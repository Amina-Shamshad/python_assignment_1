if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        operations=input().split()
        if operations[0]=='insert':
            lst.insert(int(operations[1]),int(operations[2]))
        elif operations[0]=='print':
            print(lst)
        elif operations[0]=='remove':
            lst.remove(int(operations[1]))
        elif operations[0]=='append':
            lst.append(int(operations[1]))
        elif operations[0]=='sort':
            lst.sort()
        elif operations[0]=='pop':
            lst.pop()
        elif operations[0]=='reverse':
            lst.reverse()
  