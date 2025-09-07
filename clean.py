import os


def main():
    if os.path.exists("requirements.txt"):
        os.remove("requirements.txt")

    if os.path.exists("python-exercise.zip"):
        os.remove("python-exercise.zip")


if __name__ == '__main__':
    main()
