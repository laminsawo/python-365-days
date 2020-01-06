# This lab explores basic Python assignment operators with  examples
"""
Examples include:
+=       | Equivalent to  x = x+5
-=       | Equivalent to
*=       | Equivalent to
/=       | Equivalent to

Others
%=       | Equivalent to
//=      | Equivalent to
**=      | Equivalent to
"""

# This example if short-hand for x = x+x -
x = 10
x += x
print(x)

#or
x = 10
y = 20
x += y # simplifies x = x + y
print(x)

# This example is a short-hand for x = x-x
x = 10
x -= x
print(x)

# This example is a short-hand for x = x*x
x = 5
x *= x
print(x)

# This example is a short-hand for x = x/x
x = 10
x /= x
print(x)

# This example is a short-hand for x = x % x
x = 20
x %= x
print(x)

# This example is a short-hand for x = x // x
x = 30
x //= x
print(x)

# This example is a short-hand for x = x ** x
x = 20
y = 2
x **= y
print(x)

