# Activities & Practices
print("----------------------------------")
# Practise 01
print("Practise #01")
statement_one = not (4 + 5 <= 9)
print('result of statement_one:', statement_one)
statement_two = not (8 * 2) != 20 - 4
print('result of statement_two:', statement_two)
print("----------------------------------")
# Practise 02
print("Practise #02")
credits = 120
gpa = 1.8

if not (credits >= 120):
  print("You do not have enough credits to graduate.")

if not (gpa >= 2.0):
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")    
print("----------------------------------")
# Practise 03
print("Practise #03")
# if (statement) and (statement): // if True will execute what's inside
  # print("-----")

# if not (statement):  // if not True will execute what's inside
  # print("-----")
print("----------------------------------") 
# Practise 04
print("Practise #04")
donation = 700
if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")      
print("----------------------------------") 
# Practise 05
print("Practise #05")
grade = 86 
if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")
print("----------------------------------")   
# Practise 06
print("Practise #06")
print("----------------------------------") 
# Little Codey is an interplanetary space boxer, who is trying to win championship belts for various weight categories on other planets within the solar system.
#Write a space.py program that helps Codey keep track of their target weight by:
# 1. Checks which number [planet] is equal to.
# 2. It should then compute their weight on the destination planet.

#Here is the table of conversions:

#################################
#  #   Planet    Relative Gravity
#################################
#  1   Venus     0.91
#  2   Mars      0.38
#  3   Jupiter   2.34
#  4   Saturn    1.06
#  5   Uranus    0.92
#  6   Neptune   1.19
#################################

print("I have information for the following planets:\n")

print(" 1. Venus   2. Mars    3. Jupiter")
print(" 4. Saturn  5. Uranus  6. Neptune\n")

weight = 50
planet = 4

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("Your weight in planet #{} is {}".format(planet, weight))     
print("----------------------------------") 
# Practise 07
print("Practise #07")
# Create a function called [over_budget] that has five parameters named [budget], [food_bill], [electricity_bill], [internet_bill], and [rent].
# The function should return [True] if [budget] is less than the sum of the other four parameters -you've gone over budget! Return [False] otherwise. 

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if budget < (food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False 

print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True
print("----------------------------------") 
# Practise 08
print("Practise #08")
# Write a function called [largest_number] that takes three integer inputs, [x], [y], and [z].
# Have this function, as its name implies, return the largest of the three numbers.
def largest_number(x, y, z):
  return max(x, y, z)

print(largest_number(5, 10, 50))
print("----------------------------------") 
# Practise 09
print("Practise #09")
# Create a function named [not_sum_to_ten()] that has two parameters named [num1] and [num2].
# Return [True] if [num1] and [num2] do not sum to [10]. Return [False] otherwise.  
def not_sum_to_to_ten(num1, num2):
  if num1 + num2 != 10:
    return True
  else:
    return False 

print(not_sum_to_to_ten(9, -1))
# should print True
print(not_sum_to_to_ten(9, 1))
# should print False
print(not_sum_to_to_ten(5, 5))
# should print False      
print("----------------------------------") 
# Practise 09
print("Practise #09")
# Create a function named [large_power()] that takes two parameters named [base] and [exponent].
# If [base] raised to the [exponent] is greater than [5000], return [True], otherwise return [False]
def large_power(base, exponent):
  result = base ** exponent
  if result > 5000:
    return True
  else:
    return False

print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
print("----------------------------------") 
# Practise 10
print("Practise #10")
# Create a function named twice_as_large() that has two parameters named num1 and num2.
# Return True if num1 is more than double num2. Return False otherwise.
def twice_as_large(num1, num2):
  num2 = num2 * 2
  if num1 > num2:
    return True
  else:
    return False 

print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True
print("----------------------------------") 
# Practise 11
print("Practise #11")     
# Create a function called [divisible_by_ten()] that has one parameter named [num].
# The function should return [True] if [num] is divisible by [10], and [False] otherwise.
# Consider using modulo operator [%] to check for divisibility.
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False
print("----------------------------------") 
# Practise 12
print("Practise #12")        
# Create a function named [not_sum_to_ten()] that has two parameters named [num1] and [num2].
# Return [True] if [num1] and [num2] do not sum to [10]. Return [False] otherwise.
def not_sum_to_ten(num1, num2):
  if num1 + num2 != 10:
    return True
  else:
    return False 


print(not_sum_to_to_ten(9, -1))
# sholud print True
print(not_sum_to_to_ten(9, 1))
# should print False
print(not_sum_to_to_ten(5, 5))
# should print False
print("----------------------------------") 
# Practise 13
print("Practise #13")  
# Create a function named [in_range()] that has three parameters [num], [lower], and [upper].
# The function should return [True] if [num] is greater than or equal to [lower] and less than or equal to [upper]. Otherwise, return [False].
def in_range(num, lower, upper):
  if (num >= lower) and (num <= upper):
    return True 
  else:
    return False     

print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False
print("----------------------------------") 
# Practise 14
print("Practise #14")    
# Create a function named same_name() that has two parameters named [your_name] and [my_name].
# If our names are identicl, return [True]. Otherwise, return [False].
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False

print(same_name("Mohammad", "Mohammad"))
# should print True
print(same_name("Homba", "Gomba"))
# should print False
print("----------------------------------") 
# Practise 15
print("Practise #15")  
# Create a function named [always_false()] that has one parameter named [num].
# Using an if statement, your variable [num], and the operators [>], and [<], make it so your function will return [False] no matter what number is stored in [num].
# An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.

def always_false(num):
  if num < num or num > num:
    return True
  else:
    return False


print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
print("----------------------------------") 
# Practise 16
print("Practise #16")
# Create a function named [movie_review()] that has one parameter named [rating]
# If [rating] is less than or equal to [5], return ["Avoid at all costs!"]. If [rating] is between [5] and [9], return ["This one was fun."]. If [rating] is [9] or above, return ["Outstanding!"]
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating < 9:
    return "This one was fun."
  elif rating >= 9:
    return "Outstanding!"

print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."
print("----------------------------------") 
# Practise 16
print("Practise #16")
# Create a function called [max_num()] that has three parameters named [num1], [num2], and [num3].
# The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return ["It's a tie!"].
def max_num(num1, num2, num3):
  if (num1 > num2) and (num1 > num3):
    return num1
  elif (num2 > num1) and (num2 > num3):
    return num2
  elif (num3 > num1) and (num3 > num2):
    return num3
  else:
    return "It's a tie!"

print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(15, 6, 15))
# should print "It's a tie!"