import sys

score= input ("Enter numeric value of score: ")

try:
    score = float(score)

    if score > 1.0:
        print ("Bad Score")

    # Use conditional loop to display letter grade based on user-supplied score

    # Print letter grade
    elif 1.0 >= score>=.9:
        print ("Grade is A" + str(score))
    elif .9 > score>=.8:
        print ("B")
    elif .8 >score>=.7:
        print ("C")
    elif .7 >score>=.6:
        print ("D")
    elif .6 >score>=.5:
        print ("F")

except ValueError:
    print("You need to input a number")

# End program
