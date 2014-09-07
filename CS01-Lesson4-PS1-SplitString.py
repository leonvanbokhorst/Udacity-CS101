# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def find_next_split(source, splitslist):
    result = len(source)

    if len(source) == 0:  # none can be found
        return -1

    for splitchar in splitslist:
        pos = source.find(splitchar)
        if result >= pos != -1:
            result = pos

    return result


def split_string(source, splitlist):
    result = []
    nextpos = find_next_split(source, splitlist)

    while nextpos > -1:
        word = source[:nextpos]

        if word != '':
            result += [word]

        source = source[nextpos+1:]
        nextpos = find_next_split(source, splitlist)

    return result


# test find_next_split
res1 = find_next_split("This is a test-of the,string separation-code!", " ,!-")
expected = 4
assert (res1 == expected)

res1 = find_next_split("Hello, this is a test-of the,string separation-code!", " ,!-")
expected = 5
assert (res1 == expected)

res1 = find_next_split("Hello", " ,!-")
expected = 5
assert (res1 == expected)

res1 = find_next_split("", " ,!-")
expected = -1
assert (res1 == expected)


out = split_string("This is a test-of the,string separation-code!", " ,!-")
print out
# >>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code", ",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']