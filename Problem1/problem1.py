def sqrt(number):
    if number==0:
        return 0
    if number==1:
        return 1
    lower=1
    upper=number
    while lower<=upper:
        mid=(lower+upper)//2
        if mid**2==number:
            return mid
        if mid**2<number:
            lower=mid+1
            answer=mid
        elif mid**2>number:
            upper=mid-1
    return answer


# test case1
print("______TEST CASE 1_________")
print(sqrt(9)) # should print 9
print(sqrt(16)) # should print 4

print("______TEST CASE 2_________")
print(sqrt(26)) #should print 5
print(sqrt(12)) # should print 3

print("______EDGE CASE_________")
print(sqrt(0))
print(sqrt(1))
