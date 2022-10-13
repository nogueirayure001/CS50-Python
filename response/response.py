from validator_collection import checkers


def main():
    wouldbe_email = input("What's your email address? ").strip().lower()

    print('Valid' if checkers.is_email(wouldbe_email) else 'Invalid')


if __name__ == '__main__':
    main()
