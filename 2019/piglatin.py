import re
text = input()
if len(text) < 3 or len(text) > 10:
    exit()

if not re.match('[aeiou]', text[0]):
    for i in text[1:] + (text[0] + 'ay'):
        print(i, end='')
else:
    print(text + 'ay')