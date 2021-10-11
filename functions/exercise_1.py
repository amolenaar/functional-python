#
# Exercise 1:
#
# Both `reverse_text` and `upper_text` contain similar logic.
#
# Create a higher order function that contains the common
# functionality for both functions.
#


def do_with_text():  # provide correct function signature
    ...


def reverse_text():
    with open("text.txt") as text_file:
        content = text_file.read()
        return "".join(reversed(content))


def upper_text():
    with open("text.txt") as text_file:
        content = text_file.read()
        return content.upper()
