import random
import string
from uuid import uuid4

MAX_NUMBER_OF_SPACES = 10

# assume number range between -100 and 100
MAX_NUMBER = 100
MIN_NUMBER = -100

# assume the length of string is limited between 1 and 20
MIN_LENGTH = 1
MAX_LENGTH = 20

# need at least 2 characters to be alphanumeric
MIN_LENGTH_OF_ALPHANUMERIC = 2

# limitations by UUID4 max 32 characters
MAX_LENGTH_OF_ALPHANUMERIC = 32


def generate_random_real_number():
    return random.uniform(MIN_NUMBER, MAX_NUMBER)


def generate_random_integer(min_value=MIN_NUMBER, max_value=MAX_NUMBER):
    return random.randint(min_value, max_value)


def generate_alphabetical_strings():
    # only using lowercase alphabets
    length = generate_random_integer(MIN_LENGTH, MAX_LENGTH)
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))


def generate_alphanumerics():
    """Utilize UUID4, then stripping all "-" and slicing the string randomly
    Returns:
        string: an alphanumeric string
    """
    length_of_string = generate_random_integer(
        MIN_LENGTH_OF_ALPHANUMERIC, MAX_LENGTH_OF_ALPHANUMERIC
    )

    string = str(uuid4()).replace("-", "")[:length_of_string]

    # Handle case if the uuid output is not alphanumeric after slicing else just return
    if string.isdigit():
        return string + generate_alphabetical_strings()
    elif string.isalpha():
        return string + str(generate_random_integer(MIN_LENGTH, MIN_LENGTH))
    else:
        return string


def generate_alphanumerics_with_spaces():
    """Assumption: Alphanumeric string cannot have more than 10 spaces in total
    Returns:
        string: an alphanumeric string with space(s) before and after it
    """
    number_of_spaces_before = generate_random_integer(0, MAX_NUMBER_OF_SPACES)
    number_of_spaces_after = generate_random_integer(
        0, MAX_NUMBER_OF_SPACES - number_of_spaces_before
    )
    total_of_spaces = number_of_spaces_before + number_of_spaces_after
    word = " " * total_of_spaces

    # insert alphanumeric word in between the spaces
    return (
        word[:number_of_spaces_before]
        + generate_alphanumerics()
        + word[number_of_spaces_before:]
    )
