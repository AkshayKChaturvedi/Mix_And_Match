from collections import Counter
from Mix_And_Match import generate_best_match, matches_dict

vowels_list = ['A', 'E', 'I', 'O', 'U']
keypad_dict = {'2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}


def test_case_223():
    matches_res_223 = matches_dict()['223']
    best_match_res_223 = generate_best_match(matches_res_223, vowels=vowels_list)
    assert Counter(matches_res_223) == Counter(['ABD', 'ABE', 'ABF', 'ACD', 'ACE', 'ACF', 'BAD', 'BAE', 'BAF', 'BCE',
                                                'CAD', 'CAE', 'CAF', 'CBE'])
    assert best_match_res_223 == 'ABE'


def test_case_222():
    matches_res_222 = matches_dict()['222']
    best_match_res_222 = generate_best_match(matches_res_222, vowels=vowels_list)
    assert Counter(matches_res_222) == Counter(['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'])
    assert best_match_res_222 == 'ABC'


def test_case_779():
    matches_res_779 = matches_dict()['779']
    best_match_res_779 = generate_best_match(matches_res_779, vowels=vowels_list)
    assert not matches_res_779
    assert not best_match_res_779

# ------------------------------------------------------End-------------------------------------------------------------
