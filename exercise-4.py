# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


# I want to ask user for length 
triangle =  print("Enter the lengths of three side of a triangle:")
# save user answer
a = input('a: ') 
b =input('b: ')
c =input('c: ')

#print out the saved input
# print(a, b, c)

#find  out if is eaualteral, scalene, and isoscles
#compare abc to find which triange shape it is

if (a==b and b==c):
    print(f'A triangle with sides of {a}, {b} & {c} is a equalateral triangle')
elif(a != b and b != c and c != a):
     print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
else:
    print(f'A triangle with sides of {a}, {b} & {c} is a isosceles triangle')


# if equalateral = "a == b" and " b == c" :
# elif scalene = " a != b" and "a != b":
# elif isosceles = "a == b":
