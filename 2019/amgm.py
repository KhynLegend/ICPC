length = int(input())
numbers = list(map(float, input().split())) 

print(sum(numbers) / length)
base = 1
for i in numbers:
    base = base * i

print('{:.2f}'.format(base ** (1/length)))