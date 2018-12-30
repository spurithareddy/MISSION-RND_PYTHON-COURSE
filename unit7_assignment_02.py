__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import re
import sys


def vowel(wrd):
    xd = ['a', 'e', 'i', 'o', 'u']
    wrd = list(wrd)
    for i in wrd:
        if i in xd:
            return wrd.index(i)
    else:
        return 0


def wrd_cons(word):
    flag = 0
    c = word[0:1]
    if ord(c) >= 65 and ord(c) < 91:
        flag = 1
    word = word.lower()
    index = vowel(word)
    word = word[index:len(word)] + word[0:index] + 'ay'
    if word.find(',') != -1:
        y = word.find(',')
        word = word[:y] + word[y + 1:len(word)] + ','
    if word.find('.') != -1:
        z = word.find('.')
        word = word[:z] + word[z + 1:len(word)] + '.'
    if flag == 1:
        word = word.capitalize()
    return word


def piggy_game(sentance):
    res = []
    sentance = sentance.split()
    print(sentance)
    for i in sentance:
        x = wrd_cons(i)
        res.append(x)
    print(res)
    res = " ".join(res)
    return res


if __name__ == '__main__':
    xd = sys.argv[1]
    result = piggy_game(xd)
    print(result)
    #sys.exit(main())