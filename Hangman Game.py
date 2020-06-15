# Write your code here

import random
#Create the following word list:
word_list=['python','kotlin','java','javascript']


#choose a random word from it
answer = random.choice(word_list)


print("H A N G M A N")


while(True):
    print('Print Type "play" to play the game, "exit" to quit:')
    menu = input()
    
    if menu == "play":
        hidden_ans = len(answer) * '-'
        temp = list(hidden_ans)

        #user enters the wrong letter only 8 times.
        lives = 8
        guess_lst = []
        #the user has 8 chances to win the game
        while lives > 0 and hidden_ans != answer:
            
            i = 0
            print()
            print(hidden_ans)

            guess = (input("Input a letter:"))
            

            if len(guess) != 1:
                print("You should input a single letter")


            elif not(guess.islower()):
                print("It is not an ASCII lowercase letter")


            elif guess in guess_lst:
                print("You already typed this letter")
                
                
            elif guess not in answer:
                print("No such letter in the word")
                lives = lives - 1
                
            else:
                for letters in answer:
                    if guess == letters:
                        temp[i] = guess
                    i = i + 1
                hidden_ans = "".join(temp)

            guess_lst.append(guess)
            print(guess_lst)
            

        if hidden_ans == answer:
            print("You guessed the word!\nYou survived!")
        else:
            print("You are hanged!")

        print()

    elif menu == "exit":
        exit()

    else:
        print("Wrong menu")
