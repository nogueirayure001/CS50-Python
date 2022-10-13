import random


def main():
    level = get_level()

    score = play_game(level)

    print(f'Score: {score}')


def get_level():
    valid_input = False
    while not valid_input:
        try:
            level = int(input('Level: '))
        except ValueError:
            continue

        if level in [1, 2, 3]:
            valid_input = True

    return level


def play_game(level):
    score = 0
    phases_count = 0

    while phases_count < 10:
        numbers = [generate_integer(level), generate_integer(level)]
        correct_answer = sum(numbers)

        for _ in range(3):
            try:
                answer = int(input(f'{numbers[0]} + {numbers[1]} = '))
            except ValueError:
                print('EEE')
            else:
                if answer != correct_answer:
                    print('EEE')
                else:
                    score += 1
                    break

        if answer != correct_answer:
            print(f'{numbers[0]} + {numbers[1]} = {correct_answer}')

        phases_count += 1

    return score


def generate_integer(level):
    if level == 1:
        return random.randint(10 ** (level - 1), 10 ** level) - 1

    return random.randint(10 ** (level - 1), 10 ** level - 1)


if __name__ == "__main__":
    main()
