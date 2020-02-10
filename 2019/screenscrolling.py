a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in b[-a[1]:] + b[:a[0] - a[1]]:
    print(i)
