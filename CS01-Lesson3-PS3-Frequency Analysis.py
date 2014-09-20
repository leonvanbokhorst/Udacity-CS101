# Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.

def find(char, table):
    for item in table:
        if item[0] == char:
            return item
    return []


def parse(message, table):
    for c in message:
        item = find(c, table)

        if len(item) == 0:
            table.append([c, 1])
        else:
            item[1] += 1


def get_alphabet():
    string = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    for c in string:
        result.append([c, 0.0])

    return result


def init(size, lst):
    counter = 0

    while counter < size:
        lst.append(0.0)


def freq_analysis(message):
    result = []
    table = []
    alphabet = get_alphabet()
    msglen = len(message)

    parse(message, table)

    for item in table:
        founditem = find(item[0], alphabet)

        if len(founditem) == 0:
            continue

        founditem[1] = (item[1] + 0.0) / msglen

    for item in alphabet:
        result.append(item[1])

    return result


# Tests

# print freq_analysis("abcd")
# >>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]

print freq_analysis("adca")
# >>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]

# print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]
