import random


def preparing():
    """
    Preparing russian words from RUS.txt to dictionary of words.
    :return: Dictionary of words to using them in game function.
    """
    with open('RUS.txt', 'r') as words:
        words = words.readlines()
        for i in range(len(words)):
            words[i] = words[i].rstrip('\n')
        print(len(words))
        work_words = []
    for i in range(len(words)):
        if 4 < len(words[i]) < 8:
            work_words.append(words[i])

    dict_of_words = {i: [] for i in range(4, 8)}
    for i in range(len(work_words)):
        dict_of_words[len(work_words[i])].append(work_words[i])

    return dict_of_words


def game(word_to_play: dict):
    """
    It chooses a word, which will be compared to the one that a player enters.
    Five trials are given. If the entered word's length does not match the chosen word's, it does not count as a trial.
    :param word_to_play: Dictionary of words to choosing a word.
    :return: Prints with statuses of game.
    """
    word_len = random.randint(5, 7)
    current_word = random.choice(word_to_play[word_len])
    attempts = 5
    tryings = 1
    print(f'вводи слово из русского языка длинной в {word_len} букв, потому что именно такой длинны слово я загадал')
    print(f'слово которое загадал скрипт - {current_word}')
    while tryings <= attempts:
        print(f'Твое слово - ', end='')
        gamer_word = str(input())
        if current_word == gamer_word:
            print('Молодец, ты угадал слово')
            break
        else:
            if len(current_word) == len(gamer_word):
                print('-----------\nСлово не свовсем то, но:')
                tryings += 1
                for i in range(len(gamer_word)):
                    if gamer_word[i] == current_word[i]:
                        print(f'буква {gamer_word[i]} - на своем месте')
                    elif gamer_word[i] in current_word:
                        print(f'буква {gamer_word[i]} - где то в тексте есть')
                    else:
                        print(f'буквы {gamer_word[i]} в слове нет')

                print('-----------')
            else:
                print(f'Так дела не делаются, вводи слово длинной в {len(current_word)} букв')
    else:
        print()
        print('неповезло(')


if __name__ == '__main__':
    w = preparing()
    game(w)
