from letter_state import LetterState

class Wordle:
    
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    
    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []
        pass
    
    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)
    
    def guess(self, word: str):
        word = word.upper()
        result = []
        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = LetterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character == self.secret[i]
            result.append(letter)
            
        return result
        
    @property
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
    
    @property
    def attempts_left(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)
    
    @property
    def can_guess(self):
        return self.attempts_left > 0 and not self.is_solved