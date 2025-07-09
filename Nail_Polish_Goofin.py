import random

nail_polish_vibe1 = [
    "Red Hot Chili", "Mystic Lilac", "Ballet Slippers", "Midnight Express",
    "Peach Whisper", "Electric Rose", "Ocean Motion", "Mint Condition",
    "Nude Attitude", "Sun Kissed", "Cool Cucumber", "Violet Vibe"]

nail_polish_vibe2 = []
nail_polish_vibe3 = []
nail_polish_vibe4 = []
nail_polish_vibe5 = []

def polish_choosing():
    start_interaction = input("Would you like help choosing a nail color?")
    while start_interaction == "Y" or start_interaction == "y":
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
        
        helping = input("Are you satisfied with your new nail color? (y/n)")
        
        if helping == "y" or helping == "Y":
            start_interaction = "N"
            print("Goodbye!")

polish_choosing()



