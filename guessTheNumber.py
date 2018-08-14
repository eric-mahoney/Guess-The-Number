# imports the random library to python
import random

# greets the user with a message about the game
print("Hi, welcome to the 'Guess the Number' game!")
print("The CPU will guess a number between 1 - 100 and it's your job to guess it in 5 tries or less.")

def numGame():
	continue_game = 'y'
	guess = 0
	# continues to run the game while continue_game is 'y'
	while continue_game == 'y':

		# gets a random integer between 1 and 100 and stores it as a variable, random_number
		random_number = random.randint(1,101)
		print("Okay, we've got the number!\n")

		# while loop that loops while that stops after the user has guessed 5 times
		while guess < 5:
			# prompts the user to guess a number:
			userGuess = int(input('Which number would you like to guess? '))

			# if elif statement that gives user feedback based on their guesses
			if userGuess == random_number:
				print('\tWINNER')
				print('\tTHE NUMBER WAS: ' + str(random_number) + "\n")
				break
			elif userGuess > random_number:
				print('\tTOO HIGH - GUESS AGAIN')
			elif userGuess < random_number:
				print('\tTOO LOW - GUESS AGAIN')

			# increments one to the guesses after every guess:
			guess += 1

			# tells the user how many guesses they've made:
			print('\tYou have made: ' + str(guess) + " guesses")

		# tells the user if you've run out of guesses
		if guess == 5:
			print("Sorry! You ran out of guesses.")

		# askes the user to play again. 'y' will continue playing, 'n' will break the while loop
		continue_game = input("Play again? 'y' or 'n': ")

		# resets the guesses back to zero incase the user chooses to play again.
		guess = 0

numGame()