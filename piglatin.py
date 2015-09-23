# Cynthia Carter
# Intro to CS 2015
# Star Wars Name
# a program translates a word in pig latin 


eWord= input("Please enter an English word ")
vol = "aeiouAEIOU"

if eWord[0] == vol:
    print (eWord + "yay")
else:
    print (eWord [1:]+eWord [0]+ "ay")
    