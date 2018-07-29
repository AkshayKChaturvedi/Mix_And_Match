from itertools import product
from collections import Counter

vowels_list = ['A', 'E', 'I', 'O', 'U']
keypad_dict = {'2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}


# All matches of a string
def generate_matches(input_string, vowels, keypad):
    alphabet_list = [keypad[input_string[0]], keypad[input_string[1]], keypad[input_string[2]]]
    car_prod = list(product(*alphabet_list))
    matches_initial = [c for c in car_prod if
                       any(v in c for v in vowels) and all(va == 1 for va in Counter(c).values())]
    if len(matches_initial) == 0:
        return None
    matches = [''.join(mi) for mi in matches_initial]
    return matches


# All matches of all possible strings in a dictionary
def matches_dict():
    digit_list = list(keypad_dict.keys())
    digit_list_prod = list(product(digit_list, digit_list, digit_list))
    string_list_prod = [''.join(d) for d in digit_list_prod]
    matches_dict_all_strings = {s: generate_matches(s, vowels_list, keypad_dict) for s in string_list_prod}
    return matches_dict_all_strings


# Best match
def generate_best_match(matches, vowels):
    if matches:
        no_of_vowels = {m: sum(v in m for v in vowels) for m in matches}
        max_no_of_vowels = [n for n in no_of_vowels if no_of_vowels[n] == max(no_of_vowels.values())]
        good_matches = [''.join(mv) for mv in max_no_of_vowels]
        best_match = min(good_matches)
        return best_match
    return None


inp = '222'
matches_res = matches_dict()[inp]
best_match_res = generate_best_match(matches_res, vowels=vowels_list)
print('Case:', inp)
print('best match ->', best_match_res)
print('matches ->', matches_res)
