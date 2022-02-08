from letter_state import LetterState
from typing import List
from wordle_cz import Wordle
from colorama import Fore
import random


def main():
    
    word_set = load_word_set("Projects_portfolio/Python/Wordle_CZ/Word_list.txt")
    
    secret = random.choice(list(word_set))
    
    wordle = Wordle(secret)
    
    while wordle.can_guess:
        x = input("\nNapis svuj tip: ")
        
        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Slovo musi byt {wordle.WORD_LENGTH} pismen dlouhy!" + Fore.RESET)
            continue
        
        if not x in word_set:
            print(Fore.RED + f"{x} neni realne slovicko!" + Fore.RESET)
            continue
        
        wordle.attempt(x)
        display_results(wordle)
    
    if wordle.is_solved:
        print("\nDobre ty, uhadl jsi slovicko!")
    else:
        print("\nSkoda, neuhadl jsi slovicko!")
        print(f"Slovicko bylo: {wordle.secret}\n")
        
        
def display_results(wordle: Wordle):
    print("\nTvoje vysledky zatim...\n")
    if wordle.attempts_left > 4:
        print(f"Mas jeste {wordle.attempts_left} pokusu.\n")
    else:
        print(f"Mas jeste {wordle.attempts_left} pokusy.\n")
        
    lines = []
    
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)
        
    for _ in range(wordle.attempts_left):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))    
        
    draw_border(lines)
    
    
def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
            
    return word_set
        

def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)
    

def draw_border(lines: List[str], size: int=9, pad: int=1):
    
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    
    print(top_border)
    
    for line in lines:
        print("│" + space + line + space + "│")
        
    print(bottom_border)
    
    
if __name__ == '__main__':
    main()