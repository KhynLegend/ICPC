inputs = []
n = int(input())
for i in range(n):
    inputs.append(list(map(int, input().split())))

for i in range(len(inputs)):
    print(f'Student {i + 1}: {max(inputs[i])}')