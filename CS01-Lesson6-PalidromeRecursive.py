# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?


def is_palindrome(s):
    # base case
    if len(s) == 0:
        return True

    # all other cases
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])

    return False


print is_palindrome('')
# >>> True
print is_palindrome('abab')
# >>> False
print is_palindrome('amanaplanacanalpanama')
#>>> True