import math

def print_division_info(num1, num2):
  div = math.floor(num1/num2)
  rem = num1%num2 
  #“x divided by y is n remainder m”
  print(str(num1) + " divided by " + str(num2) + " is " + str(div) + " with a remainder of " + str(rem))

print_division_info(4, 3)
print_division_info(42,12)