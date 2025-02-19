# Lesson 3 Exercise 5.4

'''5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.'''

alien_colour: str = str(input("Choose beetwen green, yellow or red and write the colour of the alien here: "))

if alien_colour == "green":
    print("You have earned 5 points")
    
else:
    print("You have earned 10 points")