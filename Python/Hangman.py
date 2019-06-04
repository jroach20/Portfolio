#Jack Roach

from random import *

def hangman():
        dictionary = ["orangutan", "chameleon", "octopus", "stingray", "binturong", "ocelot", "woodchuck"]
        word = choice(dictionary)
        word_length = len(word)
        clue = word_length * ["_"]
        tries = len(word)
        letters_tried = ""
        letters_wrong = 0
        letters_wrong_list = []
        letters_right_list = []
        print("The animal's name is",word_length,"letters long")
        
        def guess_letter():
            print (" ".join(clue))
            letter = str.lower (input ("Guess a letter:"))
            letter.lower()
            print("\n")
            return letter

        def play_again():
            answer = str.lower (input("""would you like to play again?: (y/n)"""))
            if answer =="y" or answer =="yes":
                hangman()
            else:
                print ("Thank you for playing")
                exit

        while (letters_wrong != tries) and ("".join(clue) != word):
            letter=guess_letter()

            if len(letter) == word_length and letter != word:
                print ("A good guess. It was wrong, but I thought it was good. Guess again.")
                letters_wrong +=1
                
              
            if len(letter)==1 and letter.isalpha():
                if letters_tried.find(letter) != -1:
                    print ("You’ve already picked", letter,"(doesn't count)")
                else:
                    letters_tried = letters_tried + letter
                    first_index=word.find(letter)
                    if first_index == -1:
                        letters_wrong +=1
                        letters_wrong_list.append (letter)
                        print ("Sorry, "  + letter +" isn’t in there.")
                        
                    else:
                        print("Congratulations, you found:",letter,)
                        letters_right_list.append (letter)
                        for i in range(word_length):
                            if letter == word[i]:
                                clue[i] = letter
            else:
                print ("I want you to give me either a single letter or your guess as to what the animal is. What I don't I want you to give me is bullshit. (guess didn't count)")

            print ("\nletters that are wrong: ",letters_wrong_list)
            print ("Letters that are right: ",letters_right_list,"\n")
            
            tries_used= tries - letters_wrong
            print ("You have",tries_used,"tries left")
            
            if letters_wrong == tries:
                lose_condition()
            
            if letter == word or "".join(clue) == word:
                win_condition()
            
            def lose_condition():
                Final_Guess= str.lower (input("\nFinal chance... can you guess the word?: "))
                if Final_Guess == word:
                    win_condition()
                    play_again()
                else:
                    print("\nGame Over.")
                    print("The word was",word,"\n")
                    play_again()
            def win_condition():
                
                    print ("\nYou Win!")
                    print ("The word was",word,"\n")
                    play_again()
            
hangman()