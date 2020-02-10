datas = list(map(int, input().split()))
waypoints = list(map(int, input().split()))

wormholes = dict()
#Setting points
for i in range(datas[0]):
    wormholes.update({i + 1 : waypoints[i]})

#Jumps
curr_pos = datas[1]
for i in range(datas[2]):
    curr_pos = wormholes.get(curr_pos)

print(f'Location: {curr_pos}')
