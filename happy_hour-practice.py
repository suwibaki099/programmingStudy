import random 

bars = ["Playing Games", 
		"Watching Movies",
		"Eating Some Nuggets",
		"Make my Sister Angry"
		]

people = ["mark",
		"Jandy",
		"James",
		"prince"
		]	

random_bar = random.choice(bars)	
random_person = random.choice(people)	

print(f"Im {random_bar} with {random_person} while walking.")	
