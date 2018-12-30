__author__ = 'Kalyan'

rubber_duck_debugging = '''
 While this does seem like a joke, it WORKS very well in practice :). The ACT OF DESCRIBING your problem out ALOUD
 verbally or in WRITING often clarifies your thinking and takes you to the solution.

READ THESE LINKS:
 http://blog.codinghorror.com/rubber-duck-problem-solving/
 http://en.wikipedia.org/wiki/Rubber_duck_debugging

 I recommend you to work with a friend on this. DESCRIBE YOUR THINKING PROCESS OUT ALOUD to see this
 in action.
'''

# removes duplicates from input list and return a
# sorted list of the unique elements sorted by length
# there are 2 bugs, fix both of them.
def buggy_dedup_sort_by_len(input):
    if input is None:
        return None
    unique = list(set(input))
    return sorted(unique, key=len)


def test_debug_sort_by_len():
    assert ["a", "ab", "abc", "abcd"] == buggy_dedup_sort_by_len(["ab","a","abcd","a", "abc"])
    assert ["a"] == buggy_dedup_sort_by_len(["a","a"])
    assert None == buggy_dedup_sort_by_len(None)



# Identify the failing input from py test output and walk through the code
# loudly to see what is happening.

# Sort the words list in place by number of vowels in the word in descending order
# for e.g. aba -> has 2 letters which are vowels.
def vowel(input):
    count = 0
    if input is None:
        return None
    if input:
        for word in input.lower():
            if word in set("aeiou"):
                count = count + 1
        return count


def sort_by_vowel_count(input):
    if(input!=None):
        input.sort(key=vowel, reverse=True)
        return input


def single_sort_by_vc_test(input, result):
    sort_by_vowel_count(input)
    assert result == input

def test_sort_by_vowel_count():
    single_sort_by_vc_test(["engine", "ant", "aeiou"], ["aeiou", "engine", "ant"])
    single_sort_by_vc_test(["engine", "ant", "aeroplane", "key", "bcdgcdbcd"], ["aeroplane", "engine", "ant", "key", "bcdgcdbcd"])
    single_sort_by_vc_test([], [])
    single_sort_by_vc_test(None, None)
    single_sort_by_vc_test(["aunt", "engine", "aeiou"], ["aeiou", "engine", "aunt"])
    single_sort_by_vc_test(["aunt", "ENGINE", "aeiou"], ["aeiou", "ENGINE", "aunt"])

