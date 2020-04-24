import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return (-1)
    mini=None
    maxi=None
    i=0
    while i<len(ints):
        if i==0:
            maxi, mini = ints[i], ints[i]
        if maxi<ints[i]:
            maxi=ints[i]
        if mini>ints[i]:
            mini=ints[i]
        i+=1
    # print(mini, maxi)
    return (mini, maxi)


#testcase1
print("______________________________TEST CASE 1__________________________")
l = [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")

print("______________________________TEST CASE 2__________________________")
testcase = [-1, 4, 5, 0, 6, 9]
print("Pass" if ((-1, 9) == get_min_max(testcase)) else "Fail")

print("______________________________EDGE CASE __________________________")
testcase = [-1, 4, 5, 0, 6, -1, 0, 9]
print("Pass" if ((-1, 9) == get_min_max(testcase)) else "Fail")

testcase1 = [1]
print("Pass" if ((1,1) == get_min_max(testcase1)) else "Fail")

testcase2 = []
print("Pass" if (-1 == get_min_max(testcase2)) else "Fail")
