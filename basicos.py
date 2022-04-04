#Adding user input & printing with format
# work = int(input('Rate your work: '))
# leisure = int(input('Rate your leisure: '))

# dayRate = work + leisure
# print(f'Today\'s rate is: {dayRate}')

#Printing 2 variables separated with commas adds a space between them, even if they're numbers
# print(work, leisure)

#Reassigning variable's value
# var1 = 2
# var1 +=1
# print(var1)
# var1 *= 2
# print(var1)
#
# #Comparing variables
# var1 = 11
# var2 = 11
# res = var1 == var2
# print(f'Are they equal? {res}')
# res = var1 != var2
# print(f'Are they different? {res}')
#
# #Even numbers
# number = int(input('Type a number: '))
#
# if number % 2 == 0:
#     print(f'{number} is an even number')
# else:
#     print(f'{number} is an odd number')

#Logic operators
a = True
b= True
result = a and b #If both are true
print(result)
result = a or b #If any of them is true
print(result)
result = not b #True if any of them is False. It's a unary operator (only one variable).
print(result)

#Value within range
a = 10
if 8 <= a <= 20:
    print('Within range')
else:
    print('Out of range')

#Which number is greater?