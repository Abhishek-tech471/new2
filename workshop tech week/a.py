import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    a=1
    for i in range(1,n+1):
        a*=i
    return a
    
print(factorial(int(input())))