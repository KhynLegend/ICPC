text = input()

cur = 0
for i in text:
    if(str.upper(i) == 'A'):
        print(i + ' found at index ' + str(cur))
    cur += 1