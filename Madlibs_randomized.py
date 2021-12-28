




#Madlibs generator with randomized words from lists

import random

adjectives = ["easy", "small", "big", "hard", "crazy", "fun", "difficult"]
nouns = ["tree", "victory", "cloud", "people", "cat", "dog", "snow"]
verbs = ["learning", "talk", "create", "type", "code", "run", "persevere"]



adj1 = random.choice(adjectives)
adj2 = random.choice(adjectives)
noun1 = random.choice(nouns)
verb1 = random.choice(verbs)
verb2 =  random.choice(verbs)

print("Welcome to Python Madlibs!")

madlib = f"Hi, I'm John. I'm very new to programming and am trying to teach myself with udemy and freecodecamp. \
         I find it really {adj1} so far, and want to go into the field of programming eventually. \
         I really enjoy the {noun1} of solving problems that comes with programming. Still, sometimes it can feel like my brain is {verb1} when I'm stuck on a problem for a long time. \
         I enjoy {verb2} projects like this, because it's a fun way to learn. \
         Coding is {adj2} and I will be sticking with it."

print(madlib)