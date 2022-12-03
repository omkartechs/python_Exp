while (True):
    print("press enter to quit")
    a = input("enter a number: ")
    if a == 'q':
        break
    try:
        print("Trying....")
        a = int(a)
        if a>6:
            print("you have entered a number greater than 6")
    except Exception as e:
        print (f"your input resulted in an error:{e}")

print("thanks for playing this game")        