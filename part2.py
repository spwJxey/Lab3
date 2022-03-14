import math

def solve_quadratic(a, b, c):
  x1 = ((-b + math.sqrt(b**2 - 4*a*c))/(2*a))
  x2 = ((-b - math.sqrt(b**2 - 4*a*c))/(2*a))
  print("The roots of y = " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " are " + str(x1) + " and " + str(x2))

solve_quadratic(1, 1, 0)     
# should print: The roots of y = 1x^2 + 1x + 0 are 0.0 and -1.0
    
solve_quadratic(2, 3, 1)     
# should print: The roots of y = 2x^2 + 3x + 1 are -0.5 and -1.0
    
solve_quadratic(1, 0, -1)    
# should print: The roots of y = 1x^2 + 0x + -1 are 1.0 and -1.0

#an error occurs if b^2 is less than 4ac because the result would then be negative and you cant take the square root of a negative number
#this would be a runtime error (impossible instructions)