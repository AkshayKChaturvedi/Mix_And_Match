from itertools import product
from collections import Counter

keypad_dict = {'2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}


# All matches of a string
def generate_matches(input_string, keypad):

    vowels = ['A', 'E', 'I', 'O', 'U']

    alphabet_list = [keypad[input_string[0]], keypad[input_string[1]], keypad[input_string[2]]]

    car_prod = list(product(*alphabet_list))

    matches_initial = [c for c in car_prod if
                       any(v in c for v in vowels) and all(va == 1 for va in Counter(c).values())]

    if len(matches_initial) == 0:
        return None

    matches = [''.join(mi) for mi in matches_initial]

    return matches


# All matches of all possible strings in a dictionary
def matches_dict(input_string):

    if len(input_string) != 3:
        return 'Error : Please enter a 3 digit string'

    digit_list = list(keypad_dict.keys())

    if not set(input_string).issubset(digit_list):
        return 'Error : Please enter digits between 2 and 9 (both 2 and 9 included in the range)'

    digit_list_prod = list(product(digit_list, digit_list, digit_list))

    string_list_prod = [''.join(d) for d in digit_list_prod]

    # Generating dictionary of all possible 3 letter words that can be created from the 26 characters such that
    # the resultant 3 letters have at-least one vowel and has no duplicate characters
    matches_dict_all_strings = {s: generate_matches(s, keypad_dict) for s in string_list_prod}

    return matches_dict_all_strings[input_string]


# Best match
def generate_best_match(matches):

    if type(matches) == list:
        vowels = ['A', 'E', 'I', 'O', 'U']

        no_of_vowels = {m: sum(v in m for v in vowels) for m in matches}

        max_no_of_vowels = [n for n in no_of_vowels if no_of_vowels[n] == max(no_of_vowels.values())]

        good_matches = [''.join(mv) for mv in max_no_of_vowels]

        best_match = min(good_matches)

        return best_match

    if type(matches) == str:
        return 'Error'

    return None


def display_results(input_string):

    matches = matches_dict(input_string)

    best_match = generate_best_match(matches)

    print('Case:', inp)

    print('best match ->', best_match)

    print('matches ->', matches)


# Example Output
inp = '234'
display_results(inp)
