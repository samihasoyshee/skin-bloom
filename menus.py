from routines import skin_types, concerns, routines, concern_treatments
from ingredients import ingredients
from tips import tips
from basics import basics, menu


def discover_routine():
    print("""
    --------------------o------------------------
            🌿 Discover My Routine
    --------------------o-----------------------
    """)
    print("Let's get to know your skin")
    name = input("Name: ").title()
    print("""
        \nSkin Type:
        1. Oily
        2. Dry
        3. Combination
        4. Normal
        """)
    skin_type = input("> ").title()
    print("""
        \nPrimary Concern:
        1. Acne
        2. Dark Spots
        3. Dullness
        4. Redness
        5. None
        """)
    concern = input("> ").title()
    print("\nSensetive Skin?(yes/no)")
    sensetive = input(">").title()

    skin_type = skin_types[skin_type]
    concern = concerns[concern]

    profile = {
        "name" : name,
        "skin_type" : skin_type,
        "concern" : concern,
        "sensetive" : sensetive

    }
    
    print("""
        -----------------------------
        🌸 YOUR SKIN PROFILE 🌸 
        -----------------------------
        """)
    print(f"Name            : {profile['name']}")
    print(f"SKin Type       : {profile['skin_type']}")
    print(f"Primary Concern : {profile['concern']}")
    print(f"Sensetive Skin  : {profile['sensetive']}")

    print("""
        -----------------------------
            🧴Recommended Routine 
        -----------------------------
        """)
    routine = routines[profile['skin_type']]
    print("rf")
    print(f"🧼 Cleanser: {routine['Cleanser']}")
    print(f"💧 Moisturizer: {routine['Moisturizer']}")
    print(f"☀ Sunscreen: {routine['Sunscreen']}")
    treatment = concern_treatments[profile['concern']]
    print(f"✨ Treatment: {treatment}")
    
    if profile["sensetive"] == "yes".title():
        print("\n💚 Sensetive Skin Tips:")
        print("-Choose fregnance-free products.")
        print("-Avoid harsh scrubs.")
        print("-Patch test new products.")
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
        for tip in selected_tips:
            print(f"- {tip} ")
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
