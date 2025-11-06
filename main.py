import sys

from app.greeting.greetings import Greetings


def main():
    greetings = Greetings()
    result = greetings.greet(sys.argv)
    for value in result:
        print(value)


if __name__ == "__main__":
    main()
