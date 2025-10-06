# NOTES: This is a very simple work in progress for an application I am looking to expand upon for my own individual use.
# I believe it displays of some of my python abilities, and it's fun

import random

nail_polish_vibe1 = ["Black", "Brown", "Gray", "Beige"]
nail_polish_vibe2 = ["Dark Green", "Dark Blue", "Dark Purple", "Dark Red", "Burnt Orange", "Brown"]
nail_polish_vibe3 = ["Blue", "Green", "Purple", "Red", "Orange", "Silver", "Light Brown", "Light Pink", "Teal", "Mauve"]
nail_polish_vibe4 = ["Yellow", "Orange", "White", "Pink", "Light Pink", "Mint", "Light Brown"]
nail_polish_vibe5 = ["Shimmer top coat", "White", "Bright Orange", "Light Blue", "Turquoise", "Hot Pink", "Lavender", "Sparkles", "Wild Card-- Something you haven't worn in a long time"]

def polish_choosing():
    start_interaction = input("Would you like help choosing a nail color? (Yes or No )")
    while start_interaction == "Yes" or start_interaction == "yes":
        vibe_check = int(input("On a scale from 1-5, how cheerful are you feeling? 1 is the least cheerful, 5 is incredibly cheerful."))
        if vibe_check == 1:
            v1 = random.randint(0, len(nail_polish_vibe1) - 1)
            v1_polish = nail_polish_vibe1[v1]
            print('Paint your nails with ' + v1_polish + '!')
        elif vibe_check == 2:
            v2 = random.randint(0, len(nail_polish_vibe2) - 1)
            v2_polish = nail_polish_vibe2[v2]
            print('Paint your nails with ' + v2_polish + '!')
        elif vibe_check == 3:
            v3 = random.randint(0, len(nail_polish_vibe3) - 1)
            v3_polish = nail_polish_vibe3[v3]
            print('Paint your nails with ' + v3_polish + '!')
        elif vibe_check == 4:
            v4 = random.randint(0, len(nail_polish_vibe4) - 1)
            v4_polish = nail_polish_vibe4[v4]
            print('Paint your nails with ' + v4_polish + '!')
        elif vibe_check == 5:
            v5 = random.randint(0, len(nail_polish_vibe5) - 1)
            v5_polish = nail_polish_vibe5[v5]
            print('Paint your nails with ' + v5_polish + '!')
        
        helping = input("Are you satisfied with your new nail color? (Yes/No)")
        
        if helping == "yes" or helping == "Yes":
            start_interaction = "No"
            print("Awesome, goodbye!")

polish_choosing()