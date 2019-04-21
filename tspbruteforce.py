from itertools import permutations

def distance(p1, p2):
    d = (((p2[1] - p1[1]) ** 2) + ((p2[2] - p1[2]) ** 2)) ** .5
    return d

def tsp(Points):
    length = len(Points)
    min = None
    permutacje = list(permutations(range(1, length)))
  
    for perm in permutacje:
        curdist = 0
        prev = Points[0]
        for i in perm:
            curdist = curdist + distance(prev, Points[i])
            prev = Points[i]
            if min and curdist > min:
                break
        else:
            if not min or curdist < min:
                min = curdist
                minroute = perm
    return min, minroute

points = []

while True:
    try:
        line = input()
        s = line
        s1, s2, s3 = s.split()
        n = s.split()
        v1 = int(s1)
        v2 = float(s2)
        v3 = float(s3)
        t = [v1, v2, v3]
        points.append(t)
    except EOFError:
        break
    a = line.find(str(n))
    if a != -1:
        print(line)
    if line == '':
        break

#print(points)
#tsp(points)
dist, route = tsp(points)
#print("Dystans: ", dystans)
print(points[0][0])
for i in route:
    print(points[i][0])
