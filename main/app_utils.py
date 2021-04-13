import random
import string
from datetime import date
from main.variables.variables import (curse_words, default_dob)


def profanity_check(input):
    """ Checks for profanity
    Splits out words to see if any are in curse_words
    """
    for word in input.split():
        if word in curse_words:
            return True


def check_age(dob):
    """ Calculates age
    checks the age of the dob using todays date and dob
    If the DOB is not set to 01/01/1900 which is our default DOB
    If default dob is will return an empty string
    """
    if not dob == default_dob:
        today = date.today()
        age = today.year - dob.year - \
            ((today.month, today.day) < (dob.month, dob.day))
    else:
        age = 0
    return age


def check_birthday(dob):
    """ Checks to see if the date today matches the date dob date
    If so displays cake on profile
    """
    if not dob == default_dob:
        today = date.today()
        if ((today.month, today.day) == (dob.month, dob.day)):
            return True


def get_random_string(length):
    """ Generates a random string for password
    Uses the ascii letters to generate
    """
    items = string.ascii_letters
    result_str = ''.join(random.choice(items) for i in range(length))
    return result_str


def dog_liker(user_profile, user_session):
    """ Finds out if the user session details
    Are saved in the user_profies likers array
    If so will change the like button to unlike
    """
    for dogs_like in user_profile["dog_liker"]:
        if 'user' in dogs_like:
            liker_id = dogs_like['user']
            if user_session["_id"] == liker_id:
                return True
