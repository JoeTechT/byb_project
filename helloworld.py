
# Gathers users name.
name = input("Please Enter name: ")

# Checks to see if there was an input.
if name == "":
    print("\nHello World")
else:

    # If name has input then print name.
    print(f"\nHello {name}")

# Gets either a y or n.
git = input("\nHave you heard of git: ")

if git == "y":
    # If y print this.
    print("\nOh so you know git is awesome.")

elif git == "n":
    print("\nGIT IS AWESOME")

else:
    # If input is incorret print this.
    print("\nIncorrect input")
    print("\nYou dont deserve to know about git.")



print("\nGOODBYE")