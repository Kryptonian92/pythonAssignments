#!/usr/bin/python
# The following program is an excercise show students how to properly use variables, 
# create functions and display information based on the users input. 
def playAgain():
	again = raw_input("Do you want to play again? yes or no? ")
	if again == "yes":
		main()
	else:
		print ("Thank's for playing. Come back soon!")
def new():
	newWord = raw_input("how many players do you have? 1, 2, 10 or 22? ")
	if newWord == "1":
		print("You're a loner; However, I think you should play golf")
		playAgain()
	elif newWord == "2":
		print("You dont have many friends do you. I guess you should play Tennis")
		playAgain()
	elif newWord == "10":
		print("I strive to be as popular as you sir. Basketball is the sport for you")
		
		playAgain()
	elif newWord == "22":
		print("You dont have that many friends..they secretly hate you. I think you should play Football")
		playAgain()
	else: 
		print("Sorry invalid input. Enter 1, 2, 10, 14 or 22.")
		new()

def lazy():
	newLazy = raw_input("Are you sure? ")
	if newLazy == "yes":
		print ("If you insist on being lazy, then I must oblige. Good day sir.")
	elif newLazy == "no":
		new()
	else:
		print("Sorry invalid input. Enter 'yes' or 'no' ")
		lazy()
def main():
	hello = raw_input("Hello. My name is Jarvis, your personal AI assistant. Will you be playing any sports today? ")
	if hello == "yes":
		print("Fantastic! I have a few recommendations")
		new()
	elif hello == "no":
		lazy()
	else:
		print("Sorry invalid input. Enter 'yes' or 'no' ")
		main()

main()
#print (today)