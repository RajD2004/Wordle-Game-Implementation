from random import randint

class Game:

    '''
    CLASS TO REPRESENT WORDLE GAME
    INITIALIZES BOARD <LIST[LIST[STR]]>, RANDOM WORD, CURRENT ATTEMPT = 0
    HAS PRINT OVERRIDE METHOD, METHOD TO ADD WORD AND CHECK GAME STATUS
    '''

    __slots__ = ['board', 'curr_attempt', 'target_word']
    def __init__(self):
        '''
        INITIALIZES BOARD AND ATTRIBUTES
        '''
        self.board = [[0 for _ in range(5)] for _ in range(5)]
        file_name = "words.txt"
        self.curr_attempt = 0
        try:
            with open(file_name, 'r') as fp:
                wordsList = [line.strip() for line in fp]
            self.target_word = wordsList[randint(0, len(wordsList)-1)].upper()
            
        except Exception as e:
            print(e)
            exit()

    def __str__(self) -> str:

        '''
        RETURNS THE BOARD AS A SQUARE MATRIX STRING OBJECT
        '''

        main_string = ""
        for row in self.board:
            string = ""
            for i, col in enumerate(row):
                col = " " if col == 0 else col
                if i == 0:
                    string += "| " +str(col) + " | "
                else:
                    string += str(col) +" | "
            boundary = "-" * 21 + "\n"
            main_string += (string + "\n" + boundary)
            
        return main_string

    def __bool__(self) -> bool:

        '''
        VALIDATES TO SEE IF THE CURRENT ATTEMPT IS CORRECT
        GAME WILL END WHEN THIS METHOD EVALUATES TO TRUE
        '''

        player_word = ""
        if self.curr_attempt > 0:
            for char in self.board[self.curr_attempt - 1]:
                char = str(char)
                if not char.isalpha():
                    for c in char:
                        if c.isalpha() and c.isupper():
                            player_word += c
                else:
                    player_word += char
            
            for i, character in enumerate(self.target_word):
                if character != player_word[i]:
                    return False
            return True
        return False
    

    def add_word(self, word: str) -> bool:

        '''
        ADDS A NEW WORD FROM USER INPUT TO THE EXISTING BOARD
        DOES NOT ADD WORD IF IT DOES NOT HAVE 5 CHARACTERS OR DOES NOT HAVE ONLY ALPHABETS
        RETURNS TRUE IF SUCCESSFUL ELSE FALSE
        '''
        word_freq = {}
        targ_freq = self._get_frequency(self.target_word)

        if len(word) != 5:
            print("WORD TOO LONG OR SHORT !!!")
            return False
        
        for ch in word:
            if not ch.isalpha():
                print("NOT AN ACCEPTABLE WORD!!!")
                return False
        
        for i, char in enumerate(word):
            char = char.upper()
            boolean = char not in word_freq or char not in targ_freq or word_freq[char] < targ_freq[char]
            #letter correct
            if char == self.target_word[i] and boolean:
                self.board[self.curr_attempt][i] = '\033[92m' + char + '\033[0m'
                if char not in word_freq: word_freq[char] = 1
                else: word_freq[char] += 1

            #letter in wrong pos
            elif char != self.target_word[i] and char in self.target_word and boolean:
                self.board[self.curr_attempt][i] = '\033[93m' + char + '\033[0m'
                if char not in word_freq: word_freq[char] = 1
                else: word_freq[char] += 1

            #letter not in word
            if char not in self.target_word or not boolean:
                self.board[self.curr_attempt][i] = "\033[91m" + char + "\033[0m"
        
        self.curr_attempt += 1
        return True

    def _get_frequency(self, word : list | str):
        freq_dict = {}
        for char in word:
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1  

        return freq_dict      
    

