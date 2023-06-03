if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(set(arr),reverse=True)
    if n>1:
        print(arr[1])