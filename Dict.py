a = {"Key 1": {"Key 3" :2000}, "Key 2": 500}

print(a)
print(type(a))

b = a.get("Key 1",0)
c = b.get("Key 3", 0)
print(a.keys())
print(b)
print(c)

x = {1,2,3,4,5,6}
y = {1,2,3}
z = {}
common = x & y
print(common)

p = [1,[2,3],3,4,5,6]
q =[]
for i in p:
    if isinstance(i,list):
        q.extend(i)
    else :
        q.append(i)

print(q)


