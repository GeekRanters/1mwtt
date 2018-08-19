# # Day 1

# # Basic Exercises for Certification:
# # Write a program that tells you the following:
# # Hours in a year. How many hours are in a year?
# print (365*24)
# # Minutes in a decade. How many minutes are in a decade?
# print(365.25*10*24*60)
# # Your age in seconds. How many seconds old are you? 
# print((39*365+9)*24*60*60)
# # Andreea: I'm 48618000 seconds old hahaha. Calculate Andreea's age.
# print(48618000/365/60/60)

# # Day 2

# # No assignments

# # Day 3

# # Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.
# print("What's your first name?")
# fname = input()
# print("What's your middle name? (Leave blank if you have none)")
# mname = input()
# print("What's your last name?")
# lname = input()
# #print("Nice to see you, " + fname + ' ' + mname + ' ' + lname = '.')

# # Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)
# print("What's your favourite number?")
# fnumber = input()
# newnumber = int(fnumber)+1
# print('I think ' + str(newnumber) + ' is a bigger and better number.')

# #Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. 
# print("What do you want to tell your Angry Boss?")
# normal_tone = input()
# print("WHADDAYA MEAN \"" + normal_tone.upper() + "\"YOU'RE FIRED!!")

# DAY 4

# 99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”
# beercounter = 99
# while beercounter > 1:
#   print(str(beercounter) + ' bottles of beer on the wall, ' + str(beercounter) + ' bottles of beer')
#   beercounter -= 1
#   print('Take one down and pass it around, ' + str(beercounter) + ' bottles of beer on the wall.')

# print(str(beercounter) + ' bottle of beer on the wall, ' + str(beercounter) + ' bottle of beer')
# print('Take one down and pass it around, no more bottles of beer on the wall.')

# print('No more bottles of beer on the wall, no more bottles of beer.')
# print('Go to the store and buy some more, 99 bottles of beer on the wall.')

#Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL! unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back: NO, NOT SINCE 1938!
#To make your program really believable, have Grandma shout a different year each time, maybe any year at random between 1930 and 1950. (This part is optional and would be much easier if you read the section on Python’s random number generator under the Math Object.) You can’t stop talking to Grandma until you shout BYE.


# import random 

# print('Talk to Grandma')
# user_input = ''
# while user_input !='BYE':
#   user_input = input()
#   if user_input == user_input.upper():
#     year = random.randint(1930,1951)
#     print('NO, NOT SINCE ' + str(year) + '!')
#   else:
#     print('HUH, SPEAK UP GIRL!')

# Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, she could pretend not to hear you. Change your previous program so that you have to shout BYE three times in a row. Make sure to test your program: if you shout BYE three times but not in a row, you should still be talking to Grandma.


# import random 

# print('Talk to Grandma')
# user_input_array = []
# while user_input_array[-3::] !=['BYE','BYE','BYE']:
#   user_input = input()
#   user_input_array.append(user_input)
#   if user_input == user_input.upper():
#     year = random.randint(1930,1951)
#     print('NO, NOT SINCE ' + str(year) + '!')
#   else:
#     print('HUH, SPEAK UP GIRL!')

# Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them (and including them, if they are also leap years). Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!

import calendar

# start_year = int(input('What is your start year for the leap year exercise? '))
# end_year = int(input('What is your start year for the leap year exercise? '))

# years = list(range(start_year, end_year+1))
# leap_years = []

# for year in years:
#   if calendar.isleap(year):
#     leap_years.append(year)

# print(leap_years)

# Find something today in your life, that is a calculation. Go for a walk, look around the park, try to count something. Anything! And write a program about it. e.g. number of stairs, steps, windows, leaves estimated in the park, kids, dogs, estimate your books by bookshelf, toiletries, wardrobe.

# stairs_at_home = 16
# up_and_down_home_freq = 10
# stairs_at_work = 30
# up_and_down_work_freq = 6

# days_at_home = 365
# days_at_work = 210

# stairs_per_year = stairs_at_home * up_and_down_home_freq * days_at_home + stairs_at_work * up_and_down_work_freq * days_at_work
# stairs_per_week = round(stairs_per_year/52)
# stairs_per_day = round(stairs_per_year/365)

# print('Stairs per year: ' + str(stairs_per_year))
# print('Stairs per week (on average): ' + str(stairs_per_week))
# print('Stairs per day (on average): ' + str(stairs_per_day))


#Building and sorting an array. Write the program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second?

# print("We'll add words to the list until you hit ENTER and then return all your words in alphabetical order")
# list = []
# word = 'start'

# while word!='':
#   word = input()
#   list.append(word)

# list.pop()

# print(sorted(list))

# Table of contents. Write a table of contents program here. Start the program with a list holding all of the information for your table of contents (chapter names, page numbers, and so on). Then print out the information from the list in a beautifully formatted table of contents. Use string formatting such as left align, right align, center.

# chapter_1 = {
#   'name':'The beginning',
#   'page': 5
#   }
# chapter_1_1 = {
#   'name': 'The beginning - an introduction',
#   'page': 7
#   }
# chapter_1_2 = {
#   'name': 'The beginning - this is how we do it', 
#   'page': 10
#   }
# chapter_1_3 = {
#   'name': 'The beginning - summary', 
#   'page': 15}

# print('{:<10}'.format(chapter_1['name']),'{:>30}'.format(chapter_1['page']))
# print('{:<10}'.format(chapter_1_1['name']),'{:>12}'.format(chapter_1_1['page']))
# print('{:<10}'.format(chapter_1_2['name']),'{:>8}'.format(chapter_1_2['page']))
# print('{:<10}'.format(chapter_1_3['name']),'{:>21}'.format(chapter_1_3['page']))

# Write a function that prints out "moo" n times.

def print_moo(number):
  print('moo '*number)

print_moo(5)
print_moo(88)
