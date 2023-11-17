if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    update_arr=list(set(sorted(arr)))
    print(update_arr[-2])