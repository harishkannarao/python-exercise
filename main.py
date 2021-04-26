import sys

from my_module.greeting.greetings import Greetings

greetings = Greetings()
result = greetings.greet(sys.argv)
for value in result:
    print(value)
