attendees = int(input("Enter number of attendees: "))
food_choice = input("Do you prefer Vegetarian (yes/no)")


print("We recommend large hall with audio system and Veggie Delight Caterers") if attendees > 100 and food_choice == "yes"   else print("We recommend conference hall with projector and Gourmet Meals Caterers") and attendees < 100 and food_choice == "no" 
