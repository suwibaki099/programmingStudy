import random

lowercase = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

uppercase = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]

numbers = [1,2,3,4,5,6,7,8,9,0]

combine_letters = lowercase + uppercase + numbers


for i in range(1,15):
    random_password = random.choice(combine_letters)
    # random_lowercase = random.choice(lowercase)
    print(random_password, end="")
    # print(random_lowercase, end="")