import random


def main():
    level = get_positive_integer('Level: ')

    play_game(level)


def get_positive_integer(prompt):
    valid_input = False
    while not valid_input:
        try:
            level = int(input(prompt))
        except ValueError:
            pass
        else:
            if level > 0:
                valid_input = True

    return level


def play_game(level):
    answer = random.randint(1, level)

    game_finished = False
    while not game_finished:
        guess = get_positive_integer('Guess: ')

        if guess == answer:
            print('Just right!')
            game_finished = True
        elif guess < answer:
            print('Too small!')
        else:
            print('Too large!')


if __name__ == '__main__':
    main()
