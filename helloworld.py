
# Gathers users name.
name = input("Please Enter name: ")

# Checks to see if there was an input.
if name == "":
    print("\nHello World")
else:

    # If name has input then print name.
    print(f"\nHello {name}")

git = input("\nHave you heard of git (y/n): ")


if git == "y":
    print("\nSo you know git is awesome")

elif git == "n":
    print("\nGIT IS AWESOME")

else:
    print("\nYou didnt input correctly")
    print("\nYou dont get to know about git")

print("\nGOODBYE")