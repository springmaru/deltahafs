

a = []
def new_range(start, end): return list(map(lambda x : x/10, list(range(start*10,end*10+1))))

for x in new_range(-7,1):
    for y in new_range(-1,6):
        a.append(x**2+x*y+y**2+4*x-4*y+7)



print(max(a),min(a),sep = " / ")