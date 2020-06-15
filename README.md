# Hangman-Game-in-Python


About

Games can help you kill time when you’re bored. 
But before smartphones, people played games the classic way – with paper and pencil. 
Let’s recreate one such game and improve your programming skills in the process. 
In this project, you will code Hangman, a game where the player has to guess a word, letter by letter, in a limited number of attempts. 
Make a program that plays Hangman with you – and good luck with the guessing!





Learning outcomes

Best project for Python Basics: 
1) uses functions
2) loops 
3) lists
4) The Random module is a cherry on top.



Description


Let's have a brief overview of what you are going to build during this project. 

	Here is what the gameplay should look like:

	1) In the main menu, a player can choose to either play or exit the game;
	2) If the user chooses to play, the computer picks a word from a list: this will be the riddle;
	3) The computer asks the player to enter a letter that (s)he thinks is in the word;
	4) If there's no such letter in the word and this letter hasn't been tried before, 
	the computer counts it as a miss. A player can afford only up to 8 misses before the game is over;
	5) If the letter does occur in the word, the computer notifies the player. 
	If there are letters left to guess, the computer invites the player to go on.
	6) When the entire word is uncovered, it's a victory! The game calculates the final score and 
	goes back to the main menu.
  
  
  
  Example
  
  
  H A N G M A N
	Type "play" to play the game, "exit" to quit: > play
	 
	----------
	Input a letter: > a
	 
	-a-a------
	Input a letter: > i
	 
	-a-a---i--
	Input a letter: > o
	No such letter in the word
	 
	-a-a---i--
	Input a letter: > o
	You already typed this letter
	 
	-a-a---i--
	Input a letter: > p
	 
	-a-a---ip-
	Input a letter: > p
	You already typed this letter
	 
	-a-a---ip-
	Input a letter: > h
	No such letter in the word
	 
	-a-a---ip-
	Input a letter: > k
	No such letter in the word
	 
	-a-a---ip-
	Input a letter: > a
	You already typed this letter
	 
	-a-a---ip-
	Input a letter: > z
	No such letter in the word
	 
	-a-a---ipt
	Input a letter: > t
	 
	-a-a---ipt
	Input a letter: > x
	No such letter in the word
	 
	-a-a---ipt
	Input a letter: > b
	No such letter in the word
	 
	-a-a---ipt
	Input a letter: > d
	No such letter in the word
	 
	-a-a---ipt
	Input a letter: > w
	No such letter in the word
	You are hanged!
	 
	Type "play" to play the game, "exit" to quit: > exit

