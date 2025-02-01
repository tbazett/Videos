import random 
locations = [(m, n) for m in range(8) for n in range(8)]
knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

#m=random.randint(0,7)
#n=random.randint(0,7)
m=3
n=3
point = [m,n]
step_one =[]
step_two =[]
step_three=[]

for location in locations:
    for move in knight_moves:
        new_location = (location[0] + move[0], location[1] + move[1])
        if new_location == tuple(point): 
            step_one.append(location)

for location in locations:
    for move1 in knight_moves:
        for move2 in knight_moves:
            new_location = (location[0] + move1[0]+ move2[0], location[1] + move1[1]+ move2[1])
            if new_location == tuple(point) and new_location not in step_one: 
                step_two.append(location)
step_two = list(set(step_two))

for location in step_two:
    step_three.extend([(location[0] + dx, location[1] + dy) for dx, dy in knight_moves if 0 <= location[0] + dx < 8 and 0 <= location[1] + dy < 8])

step_three = list(set(step_three))


