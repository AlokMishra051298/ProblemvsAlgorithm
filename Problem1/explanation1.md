# Sqrt()
# Code Design
Here I used binary search to find out the square root of a number.
I started with check the middle value of number and 1, the mid^2 == number then return the mid value, else mid^2  either bigger than number or smaller than number.
If mid^2 > number, then we check left part of mid,
elif mid^2 < number, then we check in the right part of mid.

# Time Complexity:
> O(logn)

# Space Complexity
> O(1) - we are not using any auxiliary space
