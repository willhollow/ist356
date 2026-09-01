# write a sentinel controlled loop to input a color until "quit"
# add the color to a list and print the list each time
# do not add a color if it is already in the list
# keep a separate list of duplicate colors and print that list at the end
duplicates = []
color = input("Enter a color (or 'quit' to exit): ")
colors = []
while color != "quit":
    if color not in colors:
        colors.append(color)
        print(f"You entered the color: {color}")
    else:
        duplicates.append(color)
        print(f"Duplicate color: {color}")
    print(f"Current list of colors: {colors}")
    print(f"Current list of duplicate colors: {duplicates}")
    color = input("Enter a color (or 'quit' to exit): ")