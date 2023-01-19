#l = [3, 4, 4]
#print(l)
#print(type(l))
marks = [3, 4, 7, "omkar", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(len(marks))


print(marks[-3]) # negative index
print(marks[len(marks)-3]) # positove index

print(marks[5-3]) # positive index
print(marks[2]) # positive index

if "omkar" in marks:
    print("yes")
else:
    print("No")