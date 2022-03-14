import math 

def say_math(math_func, number):
  result = math_func(number)
  print ("The result of " + str(math_func) + " applied to " + str(number) +" is " + str(result))

say_math(math.sqrt, 4)
say_math(math.sin, 0)
say_math(math.tan, 123)