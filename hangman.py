from random import choice

MENU = 'Type "play" to play the game, "exit" to quit: '
LETTER_INPUT = "Input a letter: "
NO_LETTER = "That letter doesn't appear in the word"
REPEATED_LETTER = "You've already guessed this letter"
INCORRECT_CASE = "Please enter a lowercase English letter"
NOT_SINGLE_LETTER = "You should input a single letter"
END_GAME_LOST = "You lost!"
END_GAME_WIN = "You guessed the word!\nYou survived!"

words = ['python', 'java', 'kotlin', 'javascript']


def start_menu():
    while True:
        menu_selection = input(MENU)
        if menu_selection == 'exit':
            exit()
        if menu_selection == 'play':
            break
        else:
            continue
    return True


def start_game():
    global hangman_word
    global letters_in_word
    global try_amount
    global tried_letters
    hangman_word = choice(words)
    letters_in_word = set(hangman_word)
    try_amount = 8
    tried_letters = []


print('H A N G M A N')
start_menu()

hangman_word = choice(words)
letters_in_word = set(hangman_word)
try_amount = 8
tried_letters = []


def hangman_word_hide(word):
    word_to_guess = ''
    for i in word:
        if i not in tried_letters:
            word_to_guess += '-'
        else:
            word_to_guess += i
    return word_to_guess


def check_win(word):
    if hangman_word_hide(hangman_word) == word:
        return True


def check_case(letter):
    if letter != letter.lower() or letter.isalpha() is False:
        print(INCORRECT_CASE)
        return False


def check_answer_len(query):
    if len(query) != 1:
        print(NOT_SINGLE_LETTER)
        return False


while True:
    while try_amount > 0:
        print(f"\n{hangman_word_hide(hangman_word)}")
        if check_win(hangman_word):
            print(END_GAME_WIN)
            break
        answer = input(LETTER_INPUT)
        if check_case(answer) is False:
            check_answer_len(answer)
            continue
        if check_answer_len(answer) is False:
            continue
        if answer in tried_letters:
            print(REPEATED_LETTER)
            continue
        tried_letters.append(answer)
        if answer in letters_in_word:
            letters_in_word.discard(answer)
        else:
            try_amount -= 1
            print(NO_LETTER)

    if try_amount == 0:
        print(END_GAME_LOST)

    start_menu()
    start_game()
