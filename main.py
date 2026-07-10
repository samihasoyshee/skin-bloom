from menus import (
    discover_routine,
    ingredient_explorer,
    glow_tips,
    skincare_basics
)


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
1. 🌿 Discover My Routine
2. 🧪 Ingredient Explorer
3. 💡 Today's Glow Tip
4. 📖 Skin Care Basics
5. 🚪 Exit
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
    🌸 Thanks for visiting SkinBloom!

    Stay hydrated 💧
    Wear sunscreen ☀️
    Take care of yourself 💙

    See you again!
    """)
        break

    else:
        print("❌ Invalid choice. Please choose from 1-5.")
        input("Press Enter to continue...")


