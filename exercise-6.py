# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

# ask user for month in 3 characters and save user answer
print('Enter the month of the year (Jan - Dec) as 3 characters:')
m = input('month: ') 

# ask user for day and save user answer
day= input('Enter the day of the month: ')
day = int(day)

# w_month = ('Jan' or 'Feb' or 'Mar' or 'Dec')
# s_month = ('Mar','Apr','May','jun')
# s_month = ('jun','Jul','Aug','Sep')
# f_month = ('Sep','Oct','Nov','Dec')


# If month is Dec 21 - March 19 it is winter
if (m == 'Jan' or m=='Feb' or m=='Mar' or m=='Dec' and day <= 21) :
    print(f'{m} {day} is in winter') 
elif (m == 'Mar'or m =='Apr'or m =='May'or m =='Jun' and day <= 20) :
    print(f'{m} {day} is in Spring') 
elif(m == 'Jun'or m =='Jul'or m =='Aug'or m =='Sep' and day <= 21) :
    print(f'{m} {day} is in Summer') 
elif(m == 'Sep'or m =='Oct'or m =='Nov'or m =='Dec' and day <= 21) :
    print(f'{m} {day} is in Fall') 
else:
    print('enter valid month and date')