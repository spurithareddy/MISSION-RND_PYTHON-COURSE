__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
import string
"""def prune_either_or(sentence):
    if sentence is None:
        return None
    strr = ""
    flag = 0
    k = sentence.split()
    for i in range(len(k)):
        if k[i] == "either" and strr != "":
            strr = strr + ""
            flag = 1
        elif flag == 1 and k[i] == "or" and k[i-1] != "either" and k[i+1] != "":
            return strr[0:-1]
        else:
            strr = strr + k[i] + " "
    return sentence
    """


def prune_either_or(string):
    if not string:
        return string
    result = string.find(' either ')
    result1 = string.find(' or ')
    if (result == -1) or (result1 == -1):
        return string
    elif (result != 0) and (result1 != 0):
        if (result+7 - result1) < 0:
            return string[:result]+string[result+7:result1]
        else:
            return string
    else:
        return string





    pass


def test_prune_either_or_student():
    assert 'we could go to a movie' == prune_either_or('we could either go to a movie or a hotel')
    assert 'we could only go to a movie or a hotel but either was fine' == prune_either_or(
        'we could only go to a movie or a hotel but either was fine')
    assert 'we can bath' == prune_either_or('we can either bath or brush')
    assert 'Either I drive to the airport or I get a taxi' == prune_either_or(
        'Either I drive to the airport or I get a taxi')
    assert 'The food was neither tasty nor healthy' == prune_either_or('The food was neither tasty nor healthy')
    assert 'Neither our families nor our friends know that we are getting married!' == prune_either_or(
        'Neither our families nor our friends know that we are getting married!')
    assert 'melon or orange?' == prune_either_or('melon or orange?')
    assert 'well either of them is fine' == prune_either_or('well either of them is fine')
    assert "either this or that" == prune_either_or("either this or that")

    pass


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
