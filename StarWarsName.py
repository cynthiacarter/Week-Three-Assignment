# Cynthia Carter
# Intro to CS 2015
# Star Wars Name
# a program that predicts your Star Wars name when given a first and last name

def main ():
    
# User inputs her first last mother madian city name
    firstName = (input("Please enter you First name: "))
    lastName = (input("Please enter you Last name: "))
    madName =  (input ("Please enter your mothers maiden name: "))
    city = (input("Please enter you City name: "))

# Program prints starwars name 
    
    print ("Your Starwars First name is : ", firstName [0:3] + lastName [0:2])

   
    print ("Your Starwars last name is :", madName [0:3] + city [0:2])

main()