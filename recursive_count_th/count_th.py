'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # initialize count at zero
    count = 0

    # start conditional loop
    # base case
    if len(word) < 2:
        return 0
    # count first two letters if "th", recursively send back to count_th minus those two letters
    elif word[:2] == "th":
        count = 1 + count_th(word[2:])
    # if first two are not "th", recursively send back to count_th minus the first letter
    else:
        count = count_th(word[1:])

    return count
