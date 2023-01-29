tup =(1, 3, 4, 34, 45, 65, 3, 3,)
print (len(tup), tup)

temp = list(tup)
temp.append("Russia")
temp.pop(3)
temp[3] = "India"
tup = tuple(temp)
print(tup)

res =   tup.index(3, 4, 8)
print("Count of 3 in tup is :", res)


res =   len(tup)
print("list  in tup:", res)