import random
from routines import skin_types, concerns, routines, concern_treatments
from ingredients import ingredients
from tips import tips
from basics import basics, menu
#TODO : Add input validation in a future update


def discover_routine():
    print("""
    --------------------o------------------------
              Discover My Routine
    --------------------o-----------------------
    """)
    print("Let's get to know your skin-")
    name = input("Name: ").title()
    print("""
        \nSkin Type:
        1. Oily
        2. Dry
        3. Combination
        4. Normal
        """)
    skin_type = input("> ")

    print("""
        \nPrimary Concern:
        1. Acne
        2. Dark Spots
        3. Dullness
        4. Redness
        5. None
        """)
    
    concern = input("> ")
    
    print("\nSensitive Skin?(yes/no)")
    
    sensitive = input(">").title()

    skin_type = skin_types[skin_type]
    concern = concerns[concern]

    profile = {
        "name" : name,
        "skin_type" : skin_type,
        "concern" : concern,
        "sensitive" : sensitive

    }
    
    print("""
        -----------------------------
        🌸 YOUR SKIN PROFILE 🌸 
        -----------------------------
        """)
    print(f"Name            : {profile['name']}")
    print(f"SKin Type       : {profile['skin_type']}")
    print(f"Primary Concern : {profile['concern']}")
    print(f"Sensitive Skin  : {profile['sensitive']}")

    print("""
        -----------------------------
            Recommended Routine 
        -----------------------------
        """)
    routine = routines[profile['skin_type']]
    print(f"Cleanser: {routine['Cleanser']}")
    print(f"Moisturizer: {routine['Moisturizer']}")
    print(f"Sunscreen: {routine['Sunscreen']}")
    treatment = concern_treatments[profile['concern']]
    print(f"Treatment: {treatment}")
    
    if profile["sensitive"] == "yes".title():
        print("\n Sensitive Skin Tips:")
        print("-Choose fregnance-free products.")
        print("-Avoid harsh scrubs.")
        print("-Patch test new products.")

    print("\n Would you like to save your profile?")
    print("1. Yes")
    print("2. No")
    save = input("Input a number > "). strip()
    if save == "1":

        with open("skin_profile.txt","w") as file:
            file.write(" SkinBloom Profile \n\n")
            file.write("-------------------\n")
            file.write(f"Name: {profile['name']}\n")
            file.write(f"Skin Type: {profile['skin_type']}\n")
            file.write(f"Primary Concern: {profile['concern']}\n")
            file.write(f"Sensitive Skin: {profile['sensitive']}\n\n")
            file.write("Recommended Routine \n")
            file.write("-------------------\n")
            file.write(f"Cleanser: {routine['Cleanser']}\n")
            file.write(f"Moisturizer: {routine['Moisturizer']}\n")
            file.write(f"Sunscreen: {routine['Sunscreen']}\n")
            file.write(f"Treatment: {treatment}\n")
            if profile["sensitive"] == "Yes":
                file.write("\nSensitive Skin Tips\n")
                file.write("-------------------\n")
                file.write("- Choose fragrance-free products.\n")
                file.write("- Avoid harsh scrubs.\n")
                file.write("- Patch test new products.\n")

            print("\nYour profile has been saved successfully!")

    input("\nPress Enter to return to the main menu...")
def ingredient_explorer():
    print(""" 
        ------------------------------
            INGREDIENT EXPLORER
        ------------------------------
    """)
    print("""
    Ingredients:
    -niacinamide
    -salicylic acid
    -vitamin c
    -centella asiatica
    -hyaluronic acid
     """)
    choice1=input("Enter ingredients: ").lower()
    info=ingredients[choice1]
    print(f"\nIngredient:{choice1.title()}")
    print(f"\nBest for: {info['best_for']}")
    print(f"Benefits:{info['benefits']}")
    print(f"Avoid if: {info['avoid']}")
    input("\nPress Enter to return to the main menu...")

def glow_tips():
        print(""" 
        -----------------------------
             TODAY'S GLOW TIPS
        -----------------------------
    """)
        print("""
        -What do you want tips for?
        - Morning
        - Night
        - General
    """)
        choice2= input("Enter your choice: ").lower()
        selected_tips = tips[choice2]
        random_tip = random.choice(selected_tips)
        print("""
====================
\n Today's Glow Tip
====================
        """)
        print(random_tip)
        input("\nPress Enter to return to the main menu...")

def skincare_basics():
    while True:
            print("""
            ------------><------------
                SKINCARE BASICS
            ------------><------------
            
        """)
            
            print("""
                What do you want to know about?
                1. What is Cleanser?
                2. What is Moisturizer?
                3. What is Sunscreen?
                4. What is serum?
                5. Back

            """)
            choice3 = input("Enter your choice: ")
            if choice3 == "5":
                break
            topic = menu[choice3]
            info = basics[topic]
            print(info)
            input("\nPress Enter to return to the main menu...")



def show_main_menu():
    print("""
=============================================================================
                            🌸 SkinBloom 🌸
                     Understand your skin naturally
=============================================================================
""")

    print("Welcome to SkinBloom!")
    print("\nLet's build a skincare routine based on your skin type and concerns.")
    print("--------------------------------------------------------------------------")

    print("""
1.  Discover My Routine
2.  Ingredient Explorer
3.  Today's Glow Tip
4.  Skin Care Basics
5.  Exit
""")

while True:
    show_main_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        discover_routine()

    elif choice == "2":
        ingredient_explorer()

    elif choice == "3":
        glow_tips()

    elif choice == "4":
        skincare_basics()

    elif choice == "5":
        print("""
     Thanks for visiting SkinBloom!

    Stay hydrated 
    Wear sunscreen 
    Take care of yourself 

    See you again!
    """)
        break

    else:
        print("Invalid choice. Please choose from 1-5.")
        input("Press Enter to continue...")


