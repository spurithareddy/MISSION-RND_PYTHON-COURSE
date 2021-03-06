__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string

import operator


def anagrams(x, y):
    list1 = list(x.lower())
    list2 = list(y.lower())
    list1.sort()
    list2.sort()
    return list1 == list2


def hashing_func(key, hash_table):
    return key % len(hash_table)


def insert(hash_table, key, value):
    hash_key = hashing_func(key, hash_table)
    hash_table[hash_key].append(value)


def hash_map(lis):
    hash_table = [[] for _ in range(len(lis))]
    li = []
    li2 = []

    for k, i in enumerate(range(len(lis))):
        if lis[i] not in li:
            li.append(lis[i])
            insert(hash_table, k, lis[i])

        for j in range(i + 1, len(lis)):
            if lis[j] not in li:
                if anagrams(lis[i], lis[j]):
                    li.append(lis[j])
                    insert(hash_table, k, lis[j])

    hash_table = [x for x in hash_table if x != []]

    for i in hash_table:
        i.sort(key=lambda x: x[0].lower())
    hash_table.sort(key=lambda p: p[0].lower())
    hash_table.sort(key=len, reverse=True)

    for i in range(len(hash_table)):
        for j in range(len(hash_table[i])):
            li2.append(hash_table[i][j])

    return li2

def anagram_sort(source, destination):
    f = open(source,"r")
    f1 = open(destination,"w+")
    li = []
    for i in f:
        if i.count('#') == 0:
            if i != "\n":
                if i.count("\n") == 0:
                    i = i + "\n"
                li.append(i)
    new_list = hash_map(li)
    f.close()
    new_list = "".join(new_list)
    f1.write(new_list)
    f1.close()


    pass

def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
