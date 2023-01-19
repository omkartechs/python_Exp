#def average(a, b, c=1):
#    print ("The average is ", (a + b + c) /2)

#    average(5, 6)


def name(**name):
  print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Barnes", fname="James")