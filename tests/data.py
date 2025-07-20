import random
import string

STANDARD_LOGIN_LENGTH = 10
STANDARD_PASSWORD_LENGTH = 10
STANDARD_FIRSTNAME_LENGTH = 10

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

