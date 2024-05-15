#Task 2 and Task 3

place = input("Choose a place: forest or cave? ")
action = input("climb a tree, cross a river, light a torch, proceed in the dark?") 


if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
else:
    if place == "cave":
        if action == "light a torch":
            print("You will be able to see better!")
        elif action == "proceed in the dark":
            print("You will not see your path")
        else:
            pass
