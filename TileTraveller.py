
# https://github.com/brekimanason/TileTraveller

# Geri Fall fyrir hvert herbergi og svo hoppar notandi milli falla og þar með milli herbergja
def room1_1():
    print("You can travel (N)orth.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        room1_2()
    else:
        print("Not a valid direction!")
        room1_1()

def room1_2():
    print("You can travel: (N)orth or (E)ast or (S)outh.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        room1_3()
    elif direction == "e" or direction == "E":
        room2_2()
    elif direction == "s" or direction == "S":
        room1_1()
    else:
        print("Not a valid direction!")
        room1_2()

def room1_3():
    print("You can travel: (E)ast or (S)outh.")
    direction = input("Direction: ")
    if direction == "e" or direction == "E":
        room2_3()
    elif direction == "s" or direction == "S":
        room1_2()
    else:
        print("Not a valid direction!")
        room1_3()

def room2_1():
    print("You can travel: (N)orth.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        room2_2()
    else:
        print("Not a valid direction!")
        room2_1()

def room2_2():
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")
    if direction == "s" or direction == "S":
        room2_1()
    elif direction == "w" or direction == "W":
        room1_2()
    else:
        print("Not a valid direction!")
        room2_2()

def room2_3():
    print("You can travel: (E)ast or (W)est.")
    direction = input("Direction: ")
    if direction == "e" or direction == "E":
        room3_3()
    elif direction == "w" or direction == "W":
        room1_3()
    else:
        print("Not a valid direction!")
        room2_3()

def room3_1():
    print("Victory!")

def room3_2():
    print("You can travel: (N)orth or (S)outh.")
    direction = input("Direction: ")
    if direction == "n" or direction == "N":
        room3_3()
    elif direction == "s" or direction == "S":
        room3_1()
    else:
        print("Not a valid direction!")
        room3_2()

def room3_3():
    print("You can travel: (S)outh or (W)est.")
    direction = input("Direction: ")
    if direction == "s" or direction == "S":
        room3_2()
    elif direction == "w" or direction == "W":
        room2_3()
    else:
        print("Not a valid direction!")
        room3_3()


room1_1()