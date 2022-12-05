# SHIP 
from os import system

small_ship = 5
big_ship = 5
while True:
    system("cls")
    print("\n")
                 
    for x in range(1,11):
                if x == small_ship:
                    print( "W", end="" )
                    if x == small_ship +1 and small_ship -1:
                        print("w", end="" )
                else:
                 print( "~", end="" )
                 
                 
    print("\n")       
    option = input(">>> ")      
    # small_ship movement
    if option == "a" and small_ship > 1:  # move left
                small_ship -= 1

    if option == "d" and small_ship < 10:  # move right
                small_ship += 1      
        
    print("\n")
    if option == "x" or small_ship == 0 or small_ship == 10:  # exit
        system("cls")
        print("The Ship arrived! Congratulations!! ")
        break
