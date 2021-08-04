"""
find x^n with recursion
The base case is when n = 0, and x^0 = 1.
If n is positive and even, recursively compute y = x^n/2, and then x^n = y ⋅ y. Notice that you can get away with making just one recursive call in this case, computing x^n/2 just once, and then you multiply the result of this recursive call by itself.
If n is positive and odd, recursively compute x^n-1, so that the exponent either is 0 or is positive and even. Then, x^n = x^n-1 ⋅ x
If n is negative, recursively compute x^-n, so that the exponent becomes positive. Then, x^n = 1/x^-n.

"""

def power(x, n):
  # base case
  if n == 0:
    return 1
  # recursive case: n is negative 
  if n<0:
    return 1/power(x,-n)
  # recursive case: n is odd
  if n >0 and n%2 !=0:
    return power(x,n-1)*x
  # recursive case: n is even
  if n >0 and n%2==0:
    return power(x,n/2)*power(x,n/2)
  return None
