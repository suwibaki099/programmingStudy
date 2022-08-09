# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']
# states = ['New York', 'NY', 'Pennsylvania', 'PA', 'California', 'CA']

states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

print(states['NY'])

print(type(states))
# print(type(people))

print(states.get('FL', 'Not Found'))
print(states.get('NY', 'Not Found'))

print(states.keys())
print(states.values())

states['FL'] = 'Florida'
print(states)


# user = ['Mattan', 70, 10.5, 'Brown', 'Brown'] a list
user = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}



animal_sounds = {

   "cat": ["meow", "purr"],

   "dog": ["woof", "bark"],

   "fox": []

}




mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}

chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown', 'eyes': 'Brown'}

sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown', 'eyes': 'Brown'}

people = [mattan, chris, sarah]

for person in people:
    print(person.get('height'))






# Searching a dictionary 
# To pull out the value from a dictionary, we simply print the key. 

# If you try to access something that isn't in the dictionary, you'll get a key error. And if you ever get confused about what something is - a dictionary or a list - you can always use the type() function. 

# You can search for things in dictionaries using .get(). It lets you look something up without returning a key error. 

# You're also able to get all the keys in a given dictionary by printing .keys().

# Adding things to a dictionary is actually pretty easy. And that will set the key, even if it doesn't already exist. 

# Dictionaries are super useful to specify the information. Compare the list, which is commented out, with the dictionary, which keeps track of Mattan's details in a much more robust way: