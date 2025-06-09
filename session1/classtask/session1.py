# #  numeric data types
# both numeric data types can hold negative numbers

# # integer
# whole number
# example: 1, 2, 10, 20 ...

# float
# decimal point number:
# example: 2.3, 4.4, 4,0 ...
# bash is still easy like python, c++ is very bad

# integer_number = 10

# float_number = 5.6
# haha = 100
# print(integer_number, float_number, haha)

# addition
# subtraction
# multiplication
## division
# not space sensitive.

# print(5+      10.5    )
# print(5*10.5)
# print(5/10.5)
# print(5-10.5)
# print(10 -2 *2)
# print(10**2) # ten to the power of 2
# print(10//2) # give me the integer number, closest integer not greater than 5
# print(10%2) # give me the remainder of the division
# print(11%2) # the remainder is 1

# print('hello world 1')
# name = 'somon'
# print(type(name))
# haha = 'smiling, laughing'
# print(haha)
# number = 111
# name = 'somon'
# name1 = "somon"
# sentence = 'this is python session 1. this is an introduction to python'
# multiline_str = ''' this is line one
# this is line 2
# this is line 3
# there are no difference between single and double quotes
# we are learning data types such as integer, float, string, boolean
# now are going to learn index
# string indexing means it will refer to a place
# .
# .
# .
# '''

# word = 'hello world'
# print(word[5])
# print(word[8])
# print(word[10])
# # i can go from the back of the string with the index starting -1
# print(word[-3])
# # strint slicing
# print(word[0:5])
# print(word[6:])
# print(word[6:11])
# print(word[0:11:2])
# print(word[::3])
# print everything reverse 
# print(word[::-1])
# print(word[-1:0]) # work on this yourself
# string concatination 
# str1 = 'aKumo'
# str2 = 'haha'
# joined = str1 + ' ' + str2
# print(joined)
# print(str1 + str2, end='\n', sep='this is seperation')
# # default values for end='\n' and sep=' '
# word = 'this is line1.\nthis is line 2.\nthis is line 3.'
# print(word)
# print(len(word))

# inp = input('please provide some word: ')
# print(inp)
# inp2 = int(input('please provide a number: '))
# inp3 = int(input('please provide number 2: '))
# print(inp2 + inp3)

# inp2 = float(input('please provide a number: '))
# inp3 = float(input('please provide number 2: '))
# print(inp2 + inp3)


inp2 = int(input('please provide a number 1: '))
inp3 = int(input('please provide number 2: '))
print('multiplication result', inp2 * inp3)
print('division result', inp2/inp3)
print('modules answer', inp2%inp3)

inp4 = input('put your string here: ')
print(len(inp4))

inp5 = float(input('what is the temperature ouside today in degree celcius? '))

print(inp5*(9/5) +32)



# Python Repo Structure:
# - Step 1: Create a separate repo for python in GitHub
# - Step 2: Put all the code that you wrote in the following structure

# python repo:
#      |
#      |----> session-1
#                 |
#                 |---> classtask
#                 |           |--- session1.py
#                 |---> hometasks
#                             |--- task1.py                                                        
#                             |--- task2.py


# - Step 3: commit and push your code