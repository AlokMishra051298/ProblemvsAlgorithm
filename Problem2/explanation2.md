# Code Design
Here, again I used the binary search, but as we know that array is rotated with a pivot so, our first task is to find out the pivot, which is mainly done by find_pivot() function in our code.

1. Find_pivot()
We done our work so wisely here, we just find out mid and just check element at next of mid is if greater than element at mid then, increament mid
elif we check element at mid >= element at start, then we set start to mid+1
else, we decrement end.
It will take very less comparision to find out the pivot element.

2. then we search for the value, first in left side of pivot.
If we get the element then, we return the index,  else we check in the right side of pivot

# Time complexity
> > O(logn) - find_pivot takes negligible time to find out the pivot

# Space Complexity

>> O(1) - we used no auxiliary space to find out the element 
