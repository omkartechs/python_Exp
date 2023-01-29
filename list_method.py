l =  [1, 45, 1, 2, 4, 6]
print(l)
l.append(7)
print(l)
l.sort(reverse=True)
l.reverse()
print(l.index(1))
print(l.count(1)) # How Many time come 1
print(l)

m = l.copy()
m[0] = 0
print (l)

l.insert(1, 889)
print(l)

m = [900, 800, 1100]
k = l + m
print(k)
#l.extend(m)
print(l)


