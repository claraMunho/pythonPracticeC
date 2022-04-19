#Variable number of arguments
def nosList(*nos):
    result = 0
    for no in nos:
        result += no
    return(result)

print(nosList(1,2,3))

#kwargs: dictionary of arguments. Usually called kwargs, but can receive other names.
def listTerms(**kwargs):
    for key, value in kwargs.items():
        print(key,value)

listTerms(ole = 'nothing', pole = 'everything')
print(listTerms)

#Recursive functions
def recursive(num):
    if num == 1:
        return 1
    else:
        return num * recursive(num-1)

result = recursive(10)
print(result)

#Converse function
def kilosToProtons():
    type = input('Enter type of value: K/P')
    value = int(input('Enter value'))
    if type == 'K':
        return value * 35
    elif type == 'P':
        return value/100
    else:
        print('Incorrect type')

converted = kilosToProtons()
print(converted)