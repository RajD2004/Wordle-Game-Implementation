
#--- NEED TO FIX CASE FOR WHEN THE USER INPUTS THE WRONG FREQUENCY OF LETTERS IN THE WORD  
#--- LIKELY SHOULD USE A FREQUENCY DICTIONARY
#--- FIXED !!!
#------------------------------------------------------------------------------------------


from wordle import Game

BANNER = '''\nHELLO! WELCOME TO WORDLE

 - IF THE CHARACTER IS IN THE CORRECT POSITION IT WILL BE \033[92mGREEN\033[0m
 - IF THE CHARACTER IS \033[93mYELLOW\033[0m THEN THE CHARACTER IS PRESENT IN THE WORD BUT IN THE WRONG POSITION
 - IF THE CHARACTER \033[91mRED\033[0m IT IS NOT PRESENT IN THE WORD
 - MAKE SURE YOUR INPUT IS 5 LETTERS IN LENGTH AND ONLY CONTAINS ALPHABETS

ENJOY !!! '''

def main():
    print(BANNER)
    contin = True
    try:
        while contin:
            board = Game()
            while board.curr_attempt < 5:
                user_word = input("\nENTER YOUR 5 LETTER GUESS WORD: ")
                board.add_word(user_word)
                if board:
                    print(board)
                    print("\nGOOD JOB, YOU HAVE WON. YOUR HAVE USED {} ATTEMPTS".format(board.curr_attempt))
                    break
                print(board)
                print("\nYOU HAVE {} ATTEMPTS LEFT".format(5-board.curr_attempt))
            
            if not board:
                print("\nTHE TARGET WORD IS: {}".format(board.target_word))
                
            contin = input('\nWOULD YOU LIKE TO PLAY AGAIN (ENTER Y FOR YES): ').lower()
            contin = True if contin == 'y' else False
    #can stop execution with Ctrl+z or Ctrl+c
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass

    print("\nTHANKS FOR PLAYING :)")
        

if __name__ == "__main__":
    main()


