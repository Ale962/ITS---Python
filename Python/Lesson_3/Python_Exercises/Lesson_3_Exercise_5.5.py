# Lesson 3 Exercise 5.5

'''5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.'''

alien_colour: str = str(input("Choose beetwen green, yellow or red and write the colour of the alien here: "))

if alien_colour == "green":
    print("You have earned 5 points")

elif alien_colour == "yellow":
    print("You have earned 5 points")
    
else:
    print("You have earned 15 points")
