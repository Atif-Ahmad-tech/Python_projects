words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth','Rhino','Sloth']
counter = {}
for word in words:
    if word not in counter:
        counter[word] = 0
    counter[word] += 1
for word in counter:
    print("{}:{}".format(word, counter[word]))
# import random
 
# print("This is the number guessing game, guess a number between 10 & 100:")
# num=random.randint(10, 100)
# print(num)
# while True:
#     x=int(input())   
#     if x<num:
#         print("small, try large:")
#     elif x>num:
#         print("large ,try small:")
#     else:
#         print(f"yes u got it {x} is the right guess")
#         exit()
