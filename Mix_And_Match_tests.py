from collections import Counter
from Mix_And_Match import generate_best_match, matches_dict


def test_case_223():
    matches_res_223 = matches_dict('223')
    best_match_res_223 = generate_best_match(matches_res_223)
    assert Counter(matches_res_223) == Counter(['ABD', 'ABE', 'ABF', 'ACD', 'ACE', 'ACF', 'BAD', 'BAE', 'BAF', 'BCE',
                                                'CAD', 'CAE', 'CAF', 'CBE'])
    assert best_match_res_223 == 'ABE'


def test_case_222():
    matches_res_222 = matches_dict('222')
    best_match_res_222 = generate_best_match(matches_res_222)
    assert Counter(matches_res_222) == Counter(['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'])
    assert best_match_res_222 == 'ABC'


def test_case_779():
    matches_res_779 = matches_dict('779')
    best_match_res_779 = generate_best_match(matches_res_779)
    assert not matches_res_779
    assert not best_match_res_779


def test_error_1():
    matches_res = matches_dict('7792')
    best_match_res = generate_best_match(matches_res)
    assert matches_res == 'Error : Please enter a 3 digit string'
    assert best_match_res == 'Error'


def test_error_2():
    matches_res = matches_dict('771')
    best_match_res = generate_best_match(matches_res)
    assert matches_res == 'Error : Please enter digits between 2 and 9 (both 2 and 9 included in the range)'
    assert best_match_res == 'Error'

# ------------------------------------------------------End-------------------------------------------------------------
