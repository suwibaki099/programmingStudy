def greet(name):
    return f"Hey {name}!"

def concatenante(word_one, word_two):
    return word_one + word_two

def age_in_dog_years(age):
    result = age * 7
    return result

def reverse(text):
    return text[::-1]

def uppercase_and_reverse(text):
    return reverse(text.upper()) #called chaining in python... you call the other function


print(greet('Jandy'))
print(greet('Mark'))

print(concatenante(word_two ='Jandy', word_one ='Mark'))

print(age_in_dog_years(28))

# inside the function is called scope. they have different world inside of them.

name = 'Jandy'

def print_different_name():
    name = "Mark"
    print(name)

print(name)
print_different_name()
print(name)



print(uppercase_and_reverse('Do not go gentle into that good night.'))





# Functions are a core concept in just about any programming language. They are the most basic building blocks of programming and almost every task that a program runs happens inside a function. In this lesson, you'll learn everything you need to know about functions.

# Functions are commands (or blocks of code) that can do magical things for us! Your probably already familiar with the concept of functions if you use Excel or Google Spreadsheets. So far, we've used a bunch of functions: print(), len(), lower(). But did you know you can write your own functions?

# How to create a function in Python
# Create a file called functions.py and type: 

# def greet(name):

# The "def" defines the function that follows it. "Greet" is the name of the function. And then "name" is the argument or an input we place inside the function. Then we "return" a function that will print "Hey {name}!" 

# def greet(name):

# return f"Hey {name}!"

# Name isn't defined yet, but that's okay. We'll get to it when its called. And we can call it by typing print(greet('Mattan')). Or any other name you want. The whole thing looks like this: 

# def age_in_dog_years(age):
#     result = age * 7
   
# print(age_in_dog_years(28))

# Return is how you get back the result of whatever function your running. If you ever get a return of "None" back, it's probably because you forgot to return something. 

# It's also important to note that each function can only return one thing. If you want to return more than one thing, then you have to return a result as a list or a dictionary. You can also call functions inside of functions.

# Remember: variables and functions look the same. You know something is a variable if it doesn't have (). All functions have ().

# Dark logo @2x
