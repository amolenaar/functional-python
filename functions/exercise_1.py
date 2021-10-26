#
# Exercise 1:
#
# Both `reverse_text` and `upper_text` contain similar logic.
#
# Create a higher order function that contains the common
# functionality for both functions.
#


def do_with_text(func):
    with open("text.txt") as text_file:
        content = text_file.read()
        return func(content)

def reverse_text():
    return do_with_text(lambda content: "".join(reversed(content)))


def upper_text():
    return do_with_text(str.upper)
