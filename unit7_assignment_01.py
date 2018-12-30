__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys

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


def anagram_sort(source,file_name):
    f = open(source,"r")
    f1 = open(file_name,"w+")
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

if __name__ == "__main__":
    source = sys.argv[1]
    file_name = source[:source.find('.')] + '-results.txt'
    anagram_sort(source, file_name)
    pass
