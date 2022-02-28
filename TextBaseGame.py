#Corey Pennebaker
#The only thing was not able to finish is the 'quit' option.





#Instructions for player
def show_instructions():
    print('************* Welcome to Zombie Text Adventure Game! **************')
    print("Collect all items to kill Zombie.")
    print('Find the Zombie and then kill it, before it eats you!!')
    print('*** Move Commands: North, South, East, West')
    print("*** Add to Inventory: Y or N")
    print("*** Type 'quit' to end the game at any time.")
    print("**************************************************************")


#The dictionary links a room to other rooms
rooms = {'Dining Room': {'North': 'Bedroom', 'West': 'Garage', 'South': 'Living Room', 'East': 'Kitchen'},
         'Living Room': {'North': 'Dining Room', 'East': 'Office', 'item': 'Bullets'},
         'Office': {'West': 'Living Room', 'item': 'Gun'},
         'Garage': {'East': 'Dining Room', 'item': 'Hammer'},
         'Kitchen': {'North': 'Pantry', 'West': 'Dining Room', 'item': 'Pizza'},
         'Pantry': {'South': 'Kitchen', 'item': 'Zombie'},
         'Bedroom': {'South': 'Dining Room', 'East': 'Bathroom', 'item': 'Pillow'},
         'Bathroom': {'West': 'Bedroom', 'item': 'First Aid'}
         }

#Function call to display the game instructions
show_instructions()

#Starting room
current_room = 'Dining Room'

#Player items collected
inventory = []

#Game Loop
while True:
    if current_room == 'Pantry':
        print("\nYou are in the", current_room)
        print("Inventory:", inventory)
        print("*****************************************")
        if len(inventory) == 6:
            print("\nCongratulations! You have collected all items!")
            print("You have killed the Zombie! won the game..!!")
            break
        else:
            print("You see a Zombie! without all items.")
            print("\n...GAME OVER!")
            break
    print("\nYou are in the", current_room)
    #Pick up items
    if 'item' in rooms[current_room]:
        print("You see", rooms[current_room]['item'])
        opinion = input("Want to pick up " + rooms[current_room]['item'] + '?(Y/N): >>').upper()
        while opinion not in ['Y', 'N']:
            print("Invalid input. Try again")
            opinion = input("Want to pick up " + rooms[current_room]['item'] + '?(Y/N): >>').upper()
        if opinion == 'Y':
            inventory.append(rooms[current_room]['item'])
            del rooms[current_room]['item']

    # Items in inventory
    print("Inventory:", inventory)
    print("************************************")


    direction = input("Direction to move?(East,West,North,South): >>").title()

    if 'item' in rooms[current_room].keys():
        directions = list(rooms[current_room].keys())
        directions.remove('item')
    else:
        directions = list(rooms[current_room].keys())
    while direction not in directions:
        print("Invalid move from " + current_room + ". Try again.")
        direction = input("Direction to move?(East,West,North,South): >>").title()
    next_room = rooms[current_room][direction]
    print("You have just moved to", next_room)
    current_room = next_room


print("\nThanks for playing the game.")