day1='monday','tuesday','wednesday'
day2='thursday','friday','saturday'
day3='sunday',

day= day1+day2+day3
print(type(day)) # <class 'tuple'>
print(day) #('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
print(day*3)
# ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
#  'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
#  'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
