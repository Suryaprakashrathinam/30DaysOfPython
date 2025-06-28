# calculate factorial recursively

''' Factorial definition is
n! = n × (n-1) × (n-2) × ... × 1
Special case: 0! = 1'''

def factorial(n):
    if n==1 or n==0: return 1
    return n *factorial(n-1)
print(factorial(5))