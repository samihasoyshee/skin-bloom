from routines import routines,concern_treatments
skin_types = {
    "1" : "Oily",
    "2" : "Dry",
    "3" : "Combination",
    "4" : "Normal"
}

concerns= {
    "1" : "Acne",
    "2" : "Dark Spots",
    "3" : "Dullness",
    "4" : "Redness",
    "5" : "None"
}
print(""" 
=================================================================================
                                🌸 SkinBloom 🌸
                          Understand your skin naturally
=================================================================================
""")
print("Welcome to SkinBloom!")
print("\nLet's build a skincare routine based on your skin type and concerns.")
print( )
print("------------------------------------------------------------------------------")
print("""
\n1. 🌿 Discover My Routine"
2. 🧪 Ingredient Explorer
3. 💡 Today's Glow Tip
4. 📖 Skin Care Basics
5. 🚪 Exit
      """ )
choice = int(input("Enter your chocie: "))
if choice == 1 :
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
    routine = routines[profile["skin_type"]]
    print(f"🧼 Cleanser: {routine["Cleanser"]}")
    print(f"💧 Moisturizer: {routine["Moisturizer"]}")
    print(f"☀ Sunscreen: {routine["Sunscreen"]}")
    treatment = concern_treatments[profile["concern"]]
    print(f"✨ Treatment: {treatment}")
    
    if profile["sensetive"] == "yes".title():
        print("\n💚 Sensetive Skin Tips:")
        print("-Choose fregnance-free products.")
        print("-Avoid harsh scrubs.")
        print("-Patch test new products.")

    

        

