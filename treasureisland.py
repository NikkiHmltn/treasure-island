print("Welcome to Treasure Island. Your mission is to find the treasure.")
left_right = input("Do you go left or right?\n").lower()

if left_right == 'right':
    print("Game over!")
else: 
    swim = input("Do you swim or wait?\n").lower()
    if swim == 'swim':
        print("Game over!")
    else: 
        doors = input("You see three door. Choose red, blue, or yellow\n").lower()
        if doors == 'red':
            print("Game over!")
        elif doors == 'blue':
            print("Game over!")
        else: 
            print('You found the treasure! You win!')