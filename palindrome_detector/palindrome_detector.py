# PALINDROMY.PY
# ==============

# Importy
# ==============
import string

# Definicje
# ==============

def palindrom(word):
    """Prints whether or not the word is a palindrome?

    Args:
        word: The word or any sets od letters, symbols and numbers we would like to examine.
    
    Returns:
        if word == reverse_word: Is the word a palindrome?  
    """    
    
    word = word.lower()
    translator = str.maketrans('', '', string.punctuation)
    s = word
    word = s.translate(translator)
    reverse_word = word[::-1] 
    return word == reverse_word

def answer(word):
    """Reverses the input and provides an output answer.

    Args:
        word: The word or any sets od letters, symbols and numbers we would like to examine.
        palindrom(word): True/False

    Returns:
        print(f" Abra...): Depending on 'palindrom' T/F, prints appropriate answer
    """    

    word = word.lower()
    reverse_word = word[::-1] 

    if palindrom(word) == True:
        print(f"Abra *burps* cadabra! Yes it is a palindrome! {word.capitalize()} " + 
        f"in reverse is {reverse_word}! Magic!")
    else:
        print(f"Abra *burps* kazzam! Nope! {word.capitalize()} in reverse is " + 
        f"{reverse_word}! Not that magical!")

# Tworzymy mini-program na wzór modułu 4.3
if __name__ == "__main__":

# Użycia
# ==============

    # 0. Input
    word = input("Yes! What is it?! Speak your 'word', so that I may do my magic: ")
    # 1. "Aktywujemy 'palindrom' by uzyskać T/F"
    palindrom(word)
    # 2. "Przetwarszamy 'word' w 'reverse_word' i drukujemy odpowiedź."
    answer(word)