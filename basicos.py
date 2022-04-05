##Adding user input & printing with format
# work = int(input('Rate your work: '))
# leisure = int(input('Rate your leisure: '))

# dayRate = work + leisure
# print(f'Today\'s rate is: {dayRate}')

##Printing 2 variables separated with commas adds a space between them, even if they're numbers
# print(work, leisure)

##Reassigning variable's value
# var1 = 2
# var1 +=1
# print(var1)
# var1 *= 2
# print(var1)
#
##Comparing variables
# var1 = 11
# var2 = 11
# res = var1 == var2
# print(f'Are they equal? {res}')
# res = var1 != var2
# print(f'Are they different? {res}')
#
##Even numbers
# number = int(input('Type a number: '))
#
# if number % 2 == 0:
#     print(f'{number} is an even number')
# else:
#     print(f'{number} is an odd number')

# ##Logic operators
# a = True
# b= True
# result = a and b #If both are true
# print(result)
# result = a or b #If any of them is true
# print(result)
# result = not b #True if any of them is False. It's a unary operator (only one variable).
# print(result)
#
# ##Value within range
# a = 10
# if 8 <= a <= 20:
#     print('Within range')
# else:
#     print('Out of range')
#
# ##Which number is greater?
# # a = int(input('Number a: '))
# b = int(input('Number b: '))
# comp = a < b
# if comp:
#     print(f'Greatest number: b {b}')
# elif a == b:
#      print('Equal numbers')
# else:
#      print(f'Greatest number: a {a}')

##Warning! This is NOT a boolean unless we convert it before.
# isCheap: bool = int(input('Is it cheap? 1=Yes, 0=No  '))
# if isCheap == False:
#     print('Not a boolean! It says true because it isn\'t an empty value')
#
# if isCheap == 1:
#     isCheap = True
#     print('Now a boolean! Value: True')
# elif isCheap == 0:
#     isCheap = False
#     print('Now a boolean! Value: False')
# else:
#     print('Incorrect value')

##Simplified if
# condition = False
# print('True') if condition else print('False')

##While...
# condition = 3
# while condition < 10:
#     print(condition)
#     condition += 2
# else:
#     print('End of while')
#
# ##For in a string
# str = 'Oopsie'
#
# for i in str:
#     print(i)

##For... break. Vowels in murciegalo
# vowels = 0
# str = 'Murciegalo'
# for i in str:
#     if i == 'u' or i == 'i' or i == 'a' or i == 'e' or i == 'o':
#         vowels += 1
#         # break #If we break this, if ends the first time the condition occurs.
# else:
#     print(f'End of for. Vowels in the string: {vowels}')
#
# ##For... break. Are there aliens?
# aliensInList = 0
# tupl = ('Animal', 'Record', 'Alien')
# for i in tupl:
#     if i == 'Alien':
#         aliensInList = True
#         print(f'Warning! AliensInList = {aliensInList}')
#         break
# else:
#     print(f'It\'s OK, no aliens rn')

##For... continue. But how many aliens?
# aliensInList = 0
# tupl = ('Alien', 'Animal', 'Record', 'Alien')
# for i in tupl:
#     if i == 'Alien':
#         aliensInList += 1
#         continue ##It continues evaluating the if, even after finding the 1st occurrence.
# else:
#     print(f'We\'ve found {aliensInList} aliens')

#Playing with lists
names = ['Pierre', 'Cucu', 'Rapunzel']
print(names[0:]) #Prints all
print(names[:-1]) #Prints all but last
print(names[-1]) #Prints last
print(names[0:2]) #Prints 0 and 1, NOT 2
names.append('Meg') #Adds last
print(names[-1])
names.insert(0, 'Breixo')
print(names[0:]) #Adds but not deletes
del names[1] #Deletes
print(names)

del names #deletes the list from memory
