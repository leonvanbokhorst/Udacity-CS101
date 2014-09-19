# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.


def is_list(p):
    return isinstance(p, list)


def reverse_list(elements):
    result = []

    for item in elements:
        result.insert(0, item)

    return result


def deep_reverse(elements):
    elements = reverse_list(elements)
    result = []

    for item in elements:
        if is_list(item):
            result.append(deep_reverse(item))
        else:
            result.append(item)

    return result


# For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
# >>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q = [1, [2, 3], 4, [5, 6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]
